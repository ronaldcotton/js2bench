#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__version__ = '1.21.193' # Major, YY, Day of Year
__author__ = 'roncotton@gmail.com'

"""
js2bench.py - JetStream2 Benchmark Automation in Python

Copyright 2021 Ronald Cotton

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os
import sys
import json
import time
import numbers
import argparse
import subprocess
import platform
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def check_requirements(_os, _path):
    """ system requirements to execute """
    if _os != 'win' and _os != 'mac':
        print(f'Exiting.  {__file__} must run on Windows or MacOS.')
        sys.exit(-1)
    py_ver = float('{}.{}'.format(*sys.version_info))
    if py_ver <= 3.3:
        print(f'Exiting. Requires newer version of python3 than {py_ver}.')
        sys.exit(-2)
    if not os.path.isfile(_path):
        print(f'{_path} doesn\'t exist. Find out version of Chrome then install required file from https://chromedriver.chromium.org/downloads.')
        sys.exit(-3)
    if _os == 'win':
        chromepath = ps_command("(Get-Item (Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe').'(Default)').VersionInfo.FileName")
    else:
        chromepath = mac_command("/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --version")
    if chromepath is None:
        print(f'Chrome isn\'t installed in the default location.  Install Chrome.')


def arguments(js2_dir):
    """ parsing arguments for script """
    parser = argparse.ArgumentParser(
        description=f'JetStream2 Benchmark Automation in Python. Json results saved in {js2_dir}. See https://browserbench.org/JetStream/in-depth.html for more details.')
    parser.add_argument(
        '-i',
        '--iterations',
        type=int,
        help='Number of Iterations (launching Chrome)',
        default=int(1))
    args = parser.parse_args()
    return args.iterations


def js2_benchmark(iteration, _os, _path):
    """ main JetStream2 Benchmark using selenium and chromedriver """
    bench_site = 'https://browserbench.org/JetStream/'

    # options remove 'Devtools listening ...' output
    # https://stackoverflow.com/questions/47417581/selenium-chromedriver-how-to-disable-the-messagedevtools-on-ws/47496386
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--silent")
    options.add_argument("--log-level=3")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(_path, options=options)

    timeout = 2  # in seconds

    driver.get(bench_site)

    wait = WebDriverWait(driver, timeout)
    element = wait.until(
        EC.element_to_be_clickable(
            (By.LINK_TEXT, 'Start Test')))
    element.click()

    benchmark_list = []
    score_list = []

    # Pulls all the ids between the id=results tags
    results = driver.find_element_by_id('results')
    ids = results.find_elements_by_xpath('//*[@id]')

    # This will make a list of benchmark ids and main scores id,
    # will be used to generate a dictionary for all scores.
    getscore = False
    for _id in ids:
        single = _id.get_attribute('id')
        if getscore:
            score_list.append(single)
        if single.startswith('benchmark'):
            benchmark_list.append(single)
            getscore = True
        else:
            getscore = False

    dictionary_results = {}

    for idx, score_id in enumerate(score_list):
        result = ''
        while not isinstance(result, numbers.Number):
            time.sleep(timeout)
            element = WebDriverWait(
                driver, timeout).until(
                EC.presence_of_element_located(
                    (By.ID, score_id)))
            try:
                result = float(element.text)
            except ValueError:
                result = ''
        dictionary_results[benchmark_list[idx][10:]] = result

    result_summary = driver.find_element_by_id('result-summary')
    dictionary_results['!Benchmark_Score'] = float(
        result_summary.find_element_by_class_name("score").text)

    if _os == 'win':
        savefile = JS2_DIR + f'\\results{iteration}.json'
    else:
        savefile = JS2_DIR + f'/results{iteration}.json'

    with open(savefile, 'w') as outfile:
        json.dump(dictionary_results, outfile, indent=4, sort_keys=True)

    print(f'Benchmark Information (saved at {savefile})')
    print(dictionary_results)
    print(f'Benchmark Score: {dictionary_results["!Benchmark_Score"]}')

    driver.quit()


def ps_command(cmd):
    """ executes windows powershell commands - only one liners """
    result = subprocess.run(
        ['powershell', '-Command', cmd], capture_output=True, check=True)
    if result.returncode == 0:
        return str(result.stdout.decode('utf-8').rstrip('\r\n'))
    return None


def mac_command(cmd):
    """ executes mac commands - only one liners"""
    result = subprocess.run(
        [cmd], capture_output=True, check=True, shell=True)
    if result.returncode == 0:
        return str(result.stdout.decode('utf-8').rstrip('\n'))
    return None

def save_windows_info():
    """ collect chrome and windows info """
    system_info_dict = {}
    system_info_dict['OS'] = 'Windows'
    system_info_dict['Chrome Version'] = ps_command(
        '(Get-Item "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe").VersionInfo | Select-Object -ExpandProperty ProductVersion')
    system_info_dict['Windows Edition'] = ps_command(
        '(Get-ItemProperty "HKLM:\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion").ProductName')
    system_info_dict['Windows Build'] = ps_command('(Get-ItemProperty "HKLM:\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion").CurrentBuild') + \
        '.' + ps_command('(Get-ItemProperty "HKLM:\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion").UBR')
    system_info_dict['Windows Version'] = ps_command(
        '(Get-ItemProperty "HKLM:\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion").DisplayVersion')
    system_info_dict['Python Version'] = ps_command('python --version')[7:]

    with open(JS2_DIR + '\\sysinfo.json', 'w') as outfile:
        json.dump(system_info_dict, outfile, indent=4, sort_keys=True)

    print(f'System Information (saved at {JS2_DIR}\\sysinfo.json):')
    print(system_info_dict)


def save_mac_info():
    """ collect chrome and mac info """
    system_info_dict = {}
    system_info_dict['OS'] = 'MacOS'
    system_info_dict['Chrome Version'] = mac_command(
        '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --version')[14:].strip()
    system_info_dict['MacOS Version'] = platform.mac_ver()[0]
    system_info_dict['Python Version'] = mac_command('python3 --version')[7:]

    with open(JS2_DIR + '/sysinfo.json', 'w') as outfile:
        json.dump(system_info_dict, outfile, indent=4, sort_keys=True)

    print(f'System Information (saved at {JS2_DIR}/sysinfo.json):')
    print(system_info_dict)


if __name__ == "__main__":
    # make default results in C:\Users\<UserName>\Documents\JetStream2, if
    # doesn't exist
    _os = platform.platform()[:3].lower()
    if _os == 'win':
        _path = os.getcwd() + '\\chromedriver.exe'
    else:
        _path = os.getcwd() + '/chromedriver'
    check_requirements(_os, _path)
    if _os == 'win':
        JS2_DIR = str(Path.home()) + '\\Documents\\JetStream2'
    else:
        JS2_DIR = str(Path.home()) + '/Documents/JetStream2'
    iterations = arguments(JS2_DIR)
    Path(JS2_DIR).mkdir(parents=True, exist_ok=True)
    if _os == 'win':
        save_windows_info()
    else:
        save_mac_info()
    for i in range(1, iterations + 1):
        print(f'-- iteration {i} --')
        js2_benchmark(i, _os, _path)
