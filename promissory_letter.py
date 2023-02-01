import undetected_chromedriver as uc
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pprint import pformat

driver = uc.Chrome(enable_cdp_events=True)

def mylousyprintfunction(eventdata):
    print(pformat(eventdata))
    
# set the callback to Network.dataReceived to print (yeah not much original)
driver.add_cdp_listener("Network.dataReceived", mylousyprintfunction)
driver.get('https://www.google.com/')  # known url using cloudflare's "under attack mode"


#def mylousyprintfunction(message):
    #print(pformat(message))


# for more inspiration checkout the link below
# https://chromedevtools.github.io/devtools-protocol/1-3/Network/

# and of couse 2 lousy examples
driver.add_cdp_listener('Network.requestWillBeSent', mylousyprintfunction)
driver.add_cdp_listener('Network.dataReceived', mylousyprintfunction)

# hint: a wildcard captures all events!
# driver.add_cdp_listener('*', mylousyprintfunction)

# now all these events will be printed in my console

driver.get("https://hubspot.com/")
driver.set_window_size(1200, 1011)
driver.find_element(By.ID, "hs-eu-confirmation-button").click()
element = driver.find_element(By.CSS_SELECTOR, ".hsg-nav__group-item--order-3 .hsg-nav__link-label")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.CSS_SELECTOR, "body")
actions = ActionChains(driver)
driver.find_element(By.LINK_TEXT, "Log in").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Sign in with Google").click()
time.sleep(2)
driver.find_element(By.ID, "identifierId").click()
driver.find_element(By.ID, "identifierId").send_keys("Redouane@placement-int.com")
driver.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-vQzf8d").click()
time.sleep(2)
driver.find_element(By.NAME, "password").send_keys("nL!nUUhL6WRj0fW6")
driver.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-vQzf8d").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div/div[2]/div[1]/div/form/div[2]/button/i18n-string").click()
time.sleep(5)

#opens new window to gmail
    # Opens a new tab and switches to new tab
driver.switch_to.new_window('tab')
driver.get('https://mail.google.com/mail/u/0/#inbox')
time.sleep(10)
driver.switch_to.window(driver.window_handles[1])
time.sleep(5)
driver.find_element(By.XPATH, "//td[6]/div/div/div/div/span/span").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "h1").click()
code = driver.find_element(By.CSS_SELECTOR, "h1").text
code = code[0:6]
driver.switch_to.window(driver.window_handles[0])
time.sleep(1)
el = driver.find_element(By.ID, "code")
for character in code:
    el.send_keys(character)
    time.sleep(0.3)
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div/div[2]/div[1]/div/form/button").click()
time.sleep(5)
#opens the list with all the people that have updated their info
driver.get("https://app.hubspot.com/contacts/4209490/lists/20314/filters")
time.sleep(5)
#Promisory Letter Update - saving candidate's info
candidateName = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div/div/div/div/section/div/div/main/div/div/div[2]/div/div/div/div[1]/div/div[1]/table/tbody/tr[1]/td[2]/div/a/span/span").text
print(candidateName)
candidateEmail = driver.find_element(By.CSS_SELECTOR, ".Tr__StyledTr-sc-1p78tyf-0:nth-child(1) > .Td__StyledTd-sn3f8v-0 > .private-link").text
print(candidateEmail)
guarantorEmail = driver.find_element(By.CSS_SELECTOR, ".Tr__StyledTr-sc-1p78tyf-0:nth-child(1) > .Td__StyledTd-sn3f8v-0:nth-child(5) > .text-left").text
print(guarantorEmail)
guarantorName = driver.find_element(By.CSS_SELECTOR, ".Tr__StyledTr-sc-1p78tyf-0:nth-child(1) > .Td__StyledTd-sn3f8v-0:nth-child(6) > .text-left").text
print(guarantorName)
guarantorLastName = driver.find_element(By.CSS_SELECTOR, ".Tr__StyledTr-sc-1p78tyf-0:nth-child(1) > .Td__StyledTd-sn3f8v-0:nth-child(7) > .text-left").text
print(guarantorLastName)
driver.find_element(By.CSS_SELECTOR, ".Tr__StyledTr-sc-1p78tyf-0:nth-child(1) .private-link > .truncate-text > span").click()
time.sleep(3)
#driver.find_element(By.CSS_SELECTOR, ".uiListItem:nth-child(3) > .UniversalSidebarCard__ExpandableSectionWrapper-sc-1jrpsbe-0 i18n-string").click()
time.sleep(10)
#login into PandaDoc
driver.switch_to.new_window('tab')
driver.get('https://www.pandadoc.com/')
driver.set_window_size(1440, 786)
time.sleep(5)
driver.find_element(By.LINK_TEXT, "Log in").click()
time.sleep(3)
driver.find_element(By.ID, "email").click()
time.sleep(3)
driver.find_element(By.ID, "email").send_keys("visa@placement-int.com")
time.sleep(3)
driver.find_element(By.ID, "password").click()
time.sleep(3)
driver.find_element(By.ID, "password").send_keys("TEAMpi2020")
time.sleep(3)
driver.find_element(By.ID, "submit_button").click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[0])
time.sleep(2)
#need to add a condition: if Create Document is not visible, click here 
#driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/aside/div/div/div[1]/ul/li[3]/div/div/div[1]/div/h2/span/i18n-string")
driver.find_element(By.XPATH, "//span[contains(.,\'Create Document\')]").click()
time.sleep(15)
#fix this - there is a persistent error from here, can't click on promisory letter
driver.switch_to.frame("notifications-iframe")
#FAILING HERE 

driver.execute_script("window.scrollTo(0,0)")
print(title)
driver.find_element(By.XPATH, "//div[@id=\'templates-list-container\']/ul/li[9]/a").click()
driver.execute_script("window.scrollTo(0,0)")
driver.find_element(By.CSS_SELECTOR, ".ListItem__Title-sc-rurywq-2").click()




driver.find_element(By.XPATH, "//div[2]/div/div/div/div[2]/div/input").send_keys(vars["guarantorEmail"])
driver.find_element(By.XPATH, "//div[2]/div/div/div[2]/div/div/div/div[2]/div/input").send_keys(vars["candidateEmail"])
time.sleep(1)
vars["window_handles"] = driver.window_handles
driver.find_element(By.XPATH, "(//button[@type=\'button\'])[8]").click()
vars["win6964"] = wait_for_window(10000)
time.sleep(5)
driver.switch_to.window(vars["win6964"])
driver.switch_to.frame(5)
vars["guarantorName"] = driver.find_element(By.XPATH, "//div[2]/span[2]/span[2]/span/span/span/span").text
vars["guarantorLastName"] = driver.find_element(By.XPATH, "//div[3]/span[2]/span[2]/span/span/span").text
WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(.,\'Send\')]")))
driver.find_element(By.XPATH, "//button[contains(.,\'Send\')]").click()
driver.find_element(By.XPATH, "//div[@id=\'app\']/div/div/div/div[2]/div[2]/span/div/div/div/div/div/span[2]").click()
driver.find_element(By.XPATH, "//button[contains(.,\'Assign all\')]").click()
WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".Input-sc-1kxjdmn-0")))
driver.find_element(By.CSS_SELECTOR, ".Input-sc-1kxjdmn-0").click()
driver.find_element(By.CSS_SELECTOR, ".Input-sc-1kxjdmn-0").send_keys(vars["guarantorEmail"])
driver.find_element(By.XPATH, "//button[contains(.,\'Assign fields\')]").click()
driver.find_element(By.XPATH, "//h6[contains(.,\'Assign fields\')]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[contains(.,\'Assign fields\')]").click()
#fix
#driver.find_element(By.XPATH, "//form/div/input").send_keys("Promissory Letter Placement International for self.vars["candidateName"]")
driver.find_element(By.XPATH, "//button[contains(.,\'Save and continue\')]").click()
driver.find_element(By.XPATH, "//textarea[@type=\'text\']").click()
#fix
#driver.find_element(By.XPATH, "//textarea[@type=\'text\']").send_keys("Dear self.vars["guarantorName"] ${guarantorLastName},\\n\\nI hope this email finds you well!\\n\\nKindly find attached to this email the Promissory Letter of ${candidateName}. Please make sure to sign it accordingly and click on finish the document when all the required fields are completed.\\n\\nThank you!\\n\\n\\nThis is an automatic email!")




  



{'method': 'Network.requestWillBeSent',
 'params': {'documentURL': 'https://nowsecure.nl/',
            'frameId': 'F42BAE4BDD4E428EE2503CB5A7B4F700',
            'hasUserGesture': False,
            'initiator': {'type': 'other'},
            'loaderId': '449906A5C736D819123288133F2797E6',
            'request': {'headers': {'Upgrade-Insecure-Requests': '1',
                                    'User-Agent': 'Mozilla/5.0 (Windows NT '
                                                  '10.0; Win64; x64) '
                                                  'AppleWebKit/537.36 (KHTML, '
                                                  'like Gecko) '
                                                  'Chrome/90.0.4430.212 '
                                                  'Safari/537.36',
                                    'sec-ch-ua': '" Not A;Brand";v="99", '
                                                 '"Chromium";v="90", "Google '
                                                 'Chrome";v="90"',
                                    'sec-ch-ua-mobile': '?0'},
                        'initialPriority': 'VeryHigh',
                        'method': 'GET',
                        'mixedContentType': 'none',
                        'referrerPolicy': 'strict-origin-when-cross-origin',
                        'url': 'https://nowsecure.nl/'},
            'requestId': '449906A5C736D819123288133F2797E6',
            'timestamp': 190010.996717,
            'type': 'Document',
            'wallTime': 1621835932.112026}}
{'method': 'Network.requestWillBeSentExtraInfo',
 'params': {'associatedCookies': [],
            'headers': {':authority': 'nowsecure.nl',
                        ':method': 'GET',
                        ':path': '/',
                        ':scheme': 'https',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'en-US,en;q=0.9',
                        'sec-ch-ua': '" Not A;Brand";v="99", '
                                     '"Chromium";v="90", "Google '
                                     'Chrome";v="90"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-fetch-dest': 'document',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'none',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; '
                                      'x64) AppleWebKit/537.36 (KHTML, like '
                                      'Gecko) Chrome/90.0.4430.212 '
                                      'Safari/537.36'},
            'requestId': '449906A5C736D819123288133F2797E6'}}
{'method': 'Network.responseReceivedExtraInfo',
 'params': {'blockedCookies': [],
            'headers': {'alt-svc': 'h3-27=":443"; ma=86400, h3-28=":443"; '
                                   'ma=86400, h3-29=":443"; ma=86400',
                        'cache-control': 'private, max-age=0, no-store, '
                                         'no-cache, must-revalidate, '
                                         'post-check=0, pre-check=0',
                        'cf-ray': '65444b779ae6546f-LHR',
                        'cf-request-id': '0a3e8d7eba0000546ffd3fa000000001',
                        'content-type': 'text/html; charset=UTF-8',
                        'date': 'Mon, 24 May 2021 05:58:53 GMT',
                        'expect-ct': 'max-age=604800, '
                                     'report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"',
                        'expires': 'Thu, 01 Jan 1970 00:00:01 GMT',
                        'nel': '{"report_to":"cf-nel","max_age":604800}',
                        'permissions-policy': 'accelerometer=(),autoplay=(),camera=(),clipboard-read=(),clipboard-write=(),fullscreen=(),geolocation=(),gyroscope=(),hid=(),interest-cohort=(),magnetometer=(),microphone=(),payment=(),publickey-credentials-get=(),screen-wake-lock=(),serial=(),sync-xhr=(),usb=()',
                        'report-to': '{"endpoints":[{"url":"https:\\/\\/a.nel.cloudflare.com\\/report?s=CAfobYlmWImQ90e%2B4BFBhpPYL%2FyGyBvkcWAj%2B%2FVOLoEq0NVrD5jU9m5pi%2BKI%2BOAnINLPXOCoX2psLphA5Z38aZzWNr3eW%2BDTIK%2FQidc%3D"}],"group":"cf-nel","max_age":604800}',
                        'server': 'cloudflare',
                        'vary': 'Accept-Encoding',
                        'x-frame-options': 'SAMEORIGIN'},
            'requestId': '449906A5C736D819123288133F2797E6',
            'resourceIPAddressSpace': 'Public'}}
{'method': 'Network.responseReceived',
 'params': {'frameId': 'F42BAE4BDD4E428EE2503CB5A7B4F700',
            'loaderId': '449906A5C736D819123288133F2797E6',
            'requestId': '449906A5C736D819123288133F2797E6',
            'response': {'connectionId': 158,
                         'connectionReused': False,
                         'encodedDataLength': 851,
                         'fromDiskCache': False,
                         'fromPrefetchCache': False,
                         'fromServiceWorker': False,
                         'headers': {'alt-svc': 'h3-27=":443"; ma=86400, '
                                                'h3-28=":443"; ma=86400, '
                                                'h3-29=":443"; ma=86400',
                                     'cache-control': 'private, max-age=0, '
                                                      'no-store, no-cache, '
                                                      'must-revalidate, '
                                                      'post-check=0, '
                                                      'pre-check=0',
                                     'cf-ray': '65444b779ae6546f-LHR',
                                     'cf-request-id': '0a3e8d7eba0000546ffd3fa000000001',
                                     'content-type': 'text/html; charset=UTF-8',
                                     'date': 'Mon, 24 May 2021 05:58:53 GMT',
                                     'expect-ct': 'max-age=604800, '
                                                  'report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"',
                                     'expires': 'Thu, 01 Jan 1970 00:00:01 GMT',
                                     'nel': '{"report_to":"cf-nel","max_age":604800}',
                                     'permissions-policy': 'accelerometer=(),autoplay=(),camera=(),clipboard-read=(),clipboard-write=(),fullscreen=(),geolocation=(),gyroscope=(),hid=(),interest-cohort=(),magnetometer=(),microphone=(),payment=(),publickey-credentials-get=(),screen-wake-lock=(),serial=(),sync-xhr=(),usb=()',
                                     'report-to': '{"endpoints":[{"url":"https:\\/\\/a.nel.cloudflare.com\\/report?s=CAfobYlmWImQ90e%2B4BFBhpPYL%2FyGyBvkcWAj%2B%2FVOLoEq0NVrD5jU9m5pi%2BKI%2BOAnINLPXOCoX2psLphA5Z38aZzWNr3eW%2BDTIK%2FQidc%3D"}],"group":"cf-nel","max_age":604800}',
                                     'server': 'cloudflare',
                                     'vary': 'Accept-Encoding',
                                     'x-frame-options': 'SAMEORIGIN'},
                         'mimeType': 'text/html',
                         'protocol': 'h2',
                         'remoteIPAddress': '104.21.5.197',
                         'remotePort': 443,
                         'requestHeaders': {':authority': 'nowsecure.nl',
                                            ':method': 'GET',
                                            ':path': '/',
                                            ':scheme': 'https',
                                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                                            'accept-encoding': 'gzip, deflate, '
                                                               'br',
                                            'accept-language': 'en-US,en;q=0.9',
                                            'sec-ch-ua': '" Not '
                                                         'A;Brand";v="99", '
                                                         '"Chromium";v="90", '
                                                         '"Google '
                                                         'Chrome";v="90"',
                                            'sec-ch-ua-mobile': '?0',
                                            'sec-fetch-dest': 'document',
                                            'sec-fetch-mode': 'navigate',
                                            'sec-fetch-site': 'none',
                                            'sec-fetch-user': '?1',
                                            'upgrade-insecure-requests': '1',
                                            'user-agent': 'Mozilla/5.0 '
                                                          '(Windows NT 10.0; '
                                                          'Win64; x64) '
                                                          'AppleWebKit/537.36 '
                                                          '(KHTML, like Gecko) '
                                                          'Chrome/90.0.4430.212 '
                                                          'Safari/537.36'},
                         'responseTime': 1621835932177.923,
                         'securityDetails': {'certificateId': 0,
                                             'certificateTransparencyCompliance': 'compliant',
                                             'cipher': 'AES_128_GCM',
                                             'issuer': 'Cloudflare Inc ECC '
                                                       'CA-3',
                                             'keyExchange': '',
                                             'keyExchangeGroup': 'X25519',
                                             'protocol': 'TLS 1.3',
                                             'sanList': ['sni.cloudflaressl.com',
                                                         '*.nowsecure.nl',
                                                         'nowsecure.nl'],
                                             'signedCertificateTimestampList': [{'hashAlgorithm': 'SHA-256',
                                                                                 'logDescription': 'Google '
                                                                                                   "'Argon2021' "
                                                                                                   'log',
                                                                                 'logId': 'F65C942FD1773022145418083094568EE34D131933BFDF0C2F200BCC4EF164E3',
                                                                                 'origin': 'Embedded '
                                                                                           'in '
                                                                                           'certificate',
                                                                                 'signatureAlgorithm': 'ECDSA',
                                                                                 'signatureData': '30450221008A25458182A6E7F608FE1492086762A367381E94137952FFD621BA2E60F7E2F702203BCDEBCE1C544DECF0A113DE12B33E299319E6240426F38F08DFC04EF2E42825',
                                                                                 'status': 'Verified',
                                                                                 'timestamp': 1598706372839.0},
                                                                                {'hashAlgorithm': 'SHA-256',
                                                                                 'logDescription': 'DigiCert '
                                                                                                   'Yeti2021 '
                                                                                                   'Log',
                                                                                 'logId': '5CDC4392FEE6AB4544B15E9AD456E61037FBD5FA47DCA17394B25EE6F6C70ECA',
                                                                                 'origin': 'Embedded '
                                                                                           'in '
                                                                                           'certificate',
                                                                                 'signatureAlgorithm': 'ECDSA',
                                                                                 'signatureData': '3046022100A95A49C7435DBFC73406AC409062C27269E6E69F443A2213F3A085E3BCBD234A022100DEA878296F8A1DB43546DC1865A4C5AD2B90664A243AE0A3A6D4925802EE68A8',
                                                                                 'status': 'Verified',
                                                                                 'timestamp': 1598706372823.0}],
                                             'subjectName': 'sni.cloudflaressl.com',
                                             'validFrom': 1598659200,
                                             'validTo': 1630238400},
                         'securityState': 'secure',
                         'status': 503,
                         'statusText': '',
                         'timing': {'connectEnd': 40.414,
                                    'connectStart': 0,
                                    'dnsEnd': 0,
                                    'dnsStart': 0,
                                    'proxyEnd': -1,
                                    'proxyStart': -1,
                                    'pushEnd': 0,
                                    'pushStart': 0,
                                    'receiveHeadersEnd': 60.361,
                                    'requestTime': 190011.002239,
                                    'sendEnd': 41.348,
                                    'sendStart': 41.19,
                                    'sslEnd': 40.405,
                                    'sslStart': 10.853,
                                    'workerFetchStart': -1,
                                    'workerReady': -1,
                                    'workerRespondWithSettled': -1,
                                    'workerStart': -1},
                         'url': 'https://nowsecure.nl/'},
            'timestamp': 190011.06449,
            'type': 'Document'}}
{'method': 'Page.frameStartedLoading',
 'params': {'frameId': 'F42BAE4BDD4E428EE2503CB5A7B4F700'}}
{'method': 'Page.frameNavigated',
 'params': {'frame': {'adFrameType': 'none',
                      'crossOriginIsolatedContextType': 'NotIsolated',
                      'domainAndRegistry': 'nowsecure.nl',
                      'gatedAPIFeatures': ['SharedArrayBuffers',
                                           'SharedArrayBuffersTransferAllowed'],
                      'id': 'F42BAE4BDD4E428EE2503CB5A7B4F700',
                      'loaderId': '449906A5C736D819123288133F2797E6',
                      'mimeType': 'text/html',
                      'secureContextType': 'Secure',
                      'securityOrigin': 'https://www.google.com/',
                      'url': 'https://www.google.com/'}}}
{'method': 'Network.dataReceived',
 'params': {'dataLength': 9835,
            'encodedDataLength': 0,
            'requestId': '449906A5C736D819123288133F2797E6',
            'timestamp': 190011.093343}}
{'method': 'Network.loadingFinished',
 'params': {'encodedDataLength': 10713,
            'requestId': '449906A5C736D819123288133F2797E6',
            'shouldReportCorbBlocking': False,
            'timestamp': 190011.064011}}
{'method': 'Network.requestWillBeSent',
 'params': {'documentURL': 'https://nowsecure.nl/',
            'frameId': 'F42BAE4BDD4E428EE2503CB5A7B4F700',
            'hasUserGesture': False,
            'initiator': {'stack': {'callFrames': [{'columnNumber': 51,
                                                    'functionName': '',
                                                    'lineNumber': 114,
                                                    'scriptId': '8',
                                                    'url': 'https://nowsecure.nl/'},
                                                   {'columnNumber': 9,
                                                    'functionName': '',
                                                    'lineNumber': 115,
                                                    'scriptId': '8',
                                                    'url': 'https://nowsecure.nl/'}]},
                          'type': 'script'},
            'loaderId': '449906A5C736D819123288133F2797E6',
            'request': {'headers': {'Referer': 'https://nowsecure.nl/',
                                    'User-Agent': 'Mozilla/5.0 (Windows NT '
                                                  '10.0; Win64; x64) '
                                                  'AppleWebKit/537.36 (KHTML, '
                                                  'like Gecko) '
                                                  'Chrome/90.0.4430.212 '
                                                  'Safari/537.36',
                                    'sec-ch-ua': '" Not A;Brand";v="99", '
                                                 '"Chromium";v="90", "Google '
                                                 'Chrome";v="90"',
                                    'sec-ch-ua-mobile': '?0'},
                        'initialPriority': 'Low',
                        'method': 'GET',
                        'mixedContentType': 'none',
                        'referrerPolicy': 'strict-origin-when-cross-origin',
                        'url': 'https://nowsecure.nl/cdn-cgi/challenge-platform/h/b/orchestrate/jsch/v1?ray=65444b779ae6546f'},
            'requestId': '17180.2',
            'timestamp': 190011.106133,
            'type': 'Script',
            'wallTime': 1621835932.221325}}
{'method': 'Network.requestWillBeSent',
 'params': {'documentURL': 'https://nowsecure.nl/',
            'frameId': 'F42BAE4BDD4E428EE2503CB5A7B4F700',
            'hasUserGesture': False,
            'initiator': {'columnNumber': 13,
                          'lineNumber': 117,
                          'type': 'parser',
                          'url': 'https://nowsecure.nl/'},
            'loaderId': '449906A5C736D819123288133F2797E6',
            'request': {'headers': {'Referer': 'https://nowsecure.nl/',
                                    'User-Agent': 'Mozilla/5.0 (Windows NT '
                                                  '10.0; Win64; x64) '
                                                  'AppleWebKit/537.36 (KHTML, '
                                                  'like Gecko) '
                                                  'Chrome/90.0.4430.212 '
                                                  'Safari/537.36',
                                    'sec-ch-ua': '" Not A;Brand";v="99", '
                                                 '"Chromium";v="90", "Google '
                                                 'Chrome";v="90"',
                                    'sec-ch-ua-mobile': '?0'},
                        'initialPriority': 'Low',
                        'method': 'GET',
                        'mixedContentType': 'none',
                        'referrerPolicy': 'strict-origin-when-cross-origin',
                        'url': 'https://nowsecure.nl/cdn-cgi/images/trace/jschal/js/transparent.gif?ray=65444b779ae6546f'},
            'requestId': '17180.3',
            'timestamp': 190011.106911,
            'type': 'Image',
            'wallTime': 1621835932.222102}}
{'method': 'Network.requestWillBeSent',
 'params': {'documentURL': 'https://nowsecure.nl/',
            'frameId': 'F42BAE4BDD4E428EE2503CB5A7B4F700',
            'hasUserGesture': False,
            'initiator': {'type': 'parser', 'url': 'https://nowsecure.nl/'},
            'loaderId': '449906A5C736D819123288133F2797E6',
            'request': {'headers': {'Referer': 'https://nowsecure.nl/',
                                    'User-Agent': 'Mozilla/5.0 (Windows NT '
                                                  '10.0; Win64; x64) '
                                                  'AppleWebKit/537.36 (KHTML, '
                                                  'like Gecko) '
                                                  'Chrome/90.0.4430.212 '
                                                  'Safari/537.36',
                                    'sec-ch-ua': '" Not A;Brand";v="99", '
                                                 '"Chromium";v="90", "Google '
                                                 'Chrome";v="90"',
                                    'sec-ch-ua-mobile': '?0'},
                        'initialPriority': 'Low',
                        'method': 'GET',
                        'mixedContentType': 'none',
                        'referrerPolicy': 'strict-origin-when-cross-origin',
                        'url': 'https://nowsecure.nl/cdn-cgi/images/trace/jschal/nojs/transparent.gif?ray=65444b779ae6546f'},
            'requestId': '17180.4',
            'timestamp': 190011.109527,
            'type': 'Image',
            'wallTime': 1621835932.224719}}
{'method': 'Page.domContentEventFired', 'params': {'timestamp': 190011.110345}}
{'method': 'Network.requestWillBeSentExtraInfo',
 'params': {'associatedCookies': [],
            'clientSecurityState': {'initiatorIPAddressSpace': 'Public',
                                    'initiatorIsSecureContext': True,
                                    'privateNetworkRequestPolicy': 'WarnFromInsecureToMorePrivate'},
            'headers': {':authority': 'nowsecure.nl',
                        ':method': 'GET',
                        ':path': '/cdn-cgi/images/trace/jschal/js/transparent.gif?ray=65444b779ae6546f',
                        ':scheme': 'https',
                        'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'en-US,en;q=0.9',
                        'referer': 'https://nowsecure.nl/',
                        'sec-ch-ua': '" Not A;Brand";v="99", '
                                     '"Chromium";v="90", "Google '
                                     'Chrome";v="90"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-fetch-dest': 'image',
                        'sec-fetch-mode': 'no-cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; '
                                      'x64) AppleWebKit/537.36 (KHTML, like '
                                      'Gecko) Chrome/90.0.4430.212 '
                                      'Safari/537.36'},
            'requestId': '17180.3'}}
{'method': 'Network.requestWillBeSentExtraInfo',
 'params': {'associatedCookies': [],
            'clientSecurityState': {'initiatorIPAddressSpace': 'Public',
                                    'initiatorIsSecureContext': True,
                                    'privateNetworkRequestPolicy': 'WarnFromInsecureToMorePrivate'},
            'headers': {':authority': 'nowsecure.nl',
                        ':method': 'GET',
                        ':path': '/cdn-cgi/challenge-platform/h/b/orchestrate/jsch/v1?ray=65444b779ae6546f',
                        ':scheme': 'https',
                        'accept': '*/*',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'en-US,en;q=0.9',
                        'referer': 'https://nowsecure.nl/',
                        'sec-ch-ua': '" Not A;Brand";v="99", '
                                     '"Chromium";v="90", "Google '
                                     'Chrome";v="90"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-fetch-dest': 'script',
                        'sec-fetch-mode': 'no-cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; '
                                      'x64) AppleWebKit/537.36 (KHTML, like '
                                      'Gecko) Chrome/90.0.4430.212 '
                                      'Safari/537.36'},
            'requestId': '17180.2'}}
{'method': 'Network.requestWillBeSentExtraInfo',
 'params': {'associatedCookies': [],
            'clientSecurityState': {'initiatorIPAddressSpace': 'Public',
                                    'initiatorIsSecureContext': True,
                                    'privateNetworkRequestPolicy': 'WarnFromInsecureToMorePrivate'},
            'headers': {':authority': 'nowsecure.nl',
                        ':method': 'GET',
                        ':path': '/cdn-cgi/images/trace/jschal/nojs/transparent.gif?ray=65444b779ae6546f',
                        ':scheme': 'https',
                        'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'en-US,en;q=0.9',
                        'referer': 'https://nowsecure.nl/',
                        'sec-ch-ua': '" Not A;Brand";v="99", '
                                     '"Chromium";v="90", "Google '
                                     'Chrome";v="90"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-fetch-dest': 'image',
                        'sec-fetch-mode': 'no-cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; '
                                      'x64) AppleWebKit/537.36 (KHTML, like '
                                      'Gecko) Chrome/90.0.4430.212 '
                                      'Safari/537.36'},
            'requestId': '17180.4'}}
{'method': 'Network.responseReceivedExtraInfo',
 'params': {'blockedCookies': [],
            'headers': {'accept-ranges': 'bytes',
                        'cache-control': 'max-age=7200\npublic',
                        'cf-ray': '65444b781d1de604-LHR',
                        'content-length': '42',
                        'content-type': 'image/gif',
                        'date': 'Mon, 24 May 2021 05:58:53 GMT',
                        'etag': '"60a4d856-2a"',
                        'expires': 'Mon, 24 May 2021 07:58:53 GMT',
                        'last-modified': 'Wed, 19 May 2021 09:20:22 GMT',
                        'server': 'cloudflare',
                        'vary': 'Accept-Encoding',
                        'x-content-type-options': 'nosniff',
                        'x-frame-options': 'DENY'},
            'requestId': '17180.3',
            'resourceIPAddressSpace': 'Public'}}
{'method': 'Network.responseReceivedExtraInfo',
 'params': {'blockedCookies': [],
            'headers': {'accept-ranges': 'bytes',
                        'cache-control': 'max-age=7200\npublic',
                        'cf-ray': '65444b781d1fe604-LHR',
                        'content-length': '42',
                        'content-type': 'image/gif',
                        'date': 'Mon, 24 May 2021 05:58:53 GMT',
                        'etag': '"60a4d856-2a"',
                        'expires': 'Mon, 24 May 2021 07:58:53 GMT',
                        'last-modified': 'Wed, 19 May 2021 09:20:22 GMT',
                        'server': 'cloudflare',
                        'vary': 'Accept-Encoding',
                        'x-content-type-options': 'nosniff',
                        'x-frame-options': 'DENY'},
            'requestId': '17180.4',
            'resourceIPAddressSpace': 'Public'}}
{'method': 'Network.resourceChangedPriority',
 'params': {'newPriority': 'High',
            'requestId': '17180.4',
            'timestamp': 190011.171057}}
{'method': 'Network.responseReceived',
 'params': {'frameId': 'F42BAE4BDD4E428EE2503CB5A7B4F700',
            'loaderId': '449906A5C736D819123288133F2797E6',
            'requestId': '17180.3',
            'response': {'connectionId': 0,
                         'connectionReused': False,
                         'encodedDataLength': 214,
                         'fromDiskCache': False,
                         'fromPrefetchCache': False,
                         'fromServiceWorker': False,
                         'headers': {'accept-ranges': 'bytes',
                                     'cache-control': 'max-age=7200\npublic',
                                     'cf-ray': '65444b781d1de604-LHR',
                                     'content-length': '42',
                                     'content-type': 'image/gif',
                                     'date': 'Mon, 24 May 2021 05:58:53 GMT',
                                     'etag': '"60a4d856-2a"',
                                     'expires': 'Mon, 24 May 2021 07:58:53 GMT',
                                     'last-modified': 'Wed, 19 May 2021 '
                                                      '09:20:22 GMT',
                                     'server': 'cloudflare',
                                     'vary': 'Accept-Encoding',
                                     'x-content-type-options': 'nosniff',
                                     'x-frame-options': 'DENY'},
                         'mimeType': 'image/gif',
                         'protocol': 'h3-29',
                         'remoteIPAddress': '104.21.5.197',
                         'remotePort': 443,
                         'requestHeaders': {':authority': 'nowsecure.nl',
                                            ':method': 'GET',
                                            ':path': '/cdn-cgi/images/trace/jschal/js/transparent.gif?ray=65444b779ae6546f',
                                            ':scheme': 'https',
                                            'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
                                            'accept-encoding': 'gzip, deflate, '
                                                               'br',
                                            'accept-language': 'en-US,en;q=0.9',
                                            'referer': 'https://nowsecure.nl/',
                                            'sec-ch-ua': '" Not '
                                                         'A;Brand";v="99", '
                                                         '"Chromium";v="90", '
                                                         '"Google '
                                                         'Chrome";v="90"',
                                            'sec-ch-ua-mobile': '?0',
                                            'sec-fetch-dest': 'image',
                                            'sec-fetch-mode': 'no-cors',
                                            'sec-fetch-site': 'same-origin',
                                            'user-agent': 'Mozilla/5.0 '
                                                          '(Windows NT 10.0; '
                                                          'Win64; x64) '
                                                          'AppleWebKit/537.36 '
                                                          '(KHTML, like Gecko) '
                                                          'Chrome/90.0.4430.212 '
                                                          'Safari/537.36'},
                         'responseTime': 1621835932265.169,
                         'securityDetails': {'certificateId': 0,
                                             'certificateTransparencyCompliance': 'compliant',
                                             'cipher': 'AES_128_GCM',
                                             'issuer': 'Cloudflare Inc ECC '
                                                       'CA-3',
                                             'keyExchange': '',
                                             'keyExchangeGroup': 'X25519',
                                             'protocol': 'QUIC',
                                             'sanList': ['sni.cloudflaressl.com',
                                                         '*.nowsecure.nl',
                                                         'nowsecure.nl'],
                                             'signedCertificateTimestampList': [{'hashAlgorithm': 'SHA-256',
                                                                                 'logDescription': 'Google '
                                                                                                   "'Argon2021' "
                                                                                                   'log',
                                                                                 'logId': 'F65C942FD1773022145418083094568EE34D131933BFDF0C2F200BCC4EF164E3',
                                                                                 'origin': 'Embedded '
                                                                                           'in '
                                                                                           'certificate',
                                                                                 'signatureAlgorithm': 'ECDSA',
                                                                                 'signatureData': '30450221008A25458182A6E7F608FE1492086762A367381E94137952FFD621BA2E60F7E2F702203BCDEBCE1C544DECF0A113DE12B33E299319E6240426F38F08DFC04EF2E42825',
                                                                                 'status': 'Verified',
                                                                                 'timestamp': 1598706372839.0},
                                                                                {'hashAlgorithm': 'SHA-256',
                                                                                 'logDescription': 'DigiCert '
                                                                                                   'Yeti2021 '
                                                                                                   'Log',
                                                                                 'logId': '5CDC4392FEE6AB4544B15E9AD456E61037FBD5FA47DCA17394B25EE6F6C70ECA',
                                                                                 'origin': 'Embedded '
                                                                                           'in '
                                                                                           'certificate',
                                                                                 'signatureAlgorithm': 'ECDSA',
                                                                                 'signatureData': '3046022100A95A49C7435DBFC73406AC409062C27269E6E69F443A2213F3A085E3BCBD234A022100DEA878296F8A1DB43546DC1865A4C5AD2B90664A243AE0A3A6D4925802EE68A8',
                                                                                 'status': 'Verified',
                                                                                 'timestamp': 1598706372823.0}],
                                             'subjectName': 'sni.cloudflaressl.com',
                                             'validFrom': 1598659200,
                                             'validTo': 1630238400},
                         'securityState': 'secure',
                         'status': 200,
                         'statusText': '',
                         'timing': {'connectEnd': 26.087,
                                    'connectStart': 0,
                                    'dnsEnd': 0,
                                    'dnsStart': 0,
                                    'proxyEnd': -1,
                                    'proxyStart': -1,
                                    'pushEnd': 0,
                                    'pushStart': 0,
                                    'receiveHeadersEnd': 40.709,
                                    'requestTime': 190011.109386,
                                    'sendEnd': 26.346,
                                    'sendStart': 26.182,
                                    'sslEnd': 26.087,
                                    'sslStart': 0,
                                    'workerFetchStart': -1,
                                    'workerReady': -1,
                                    'workerRespondWithSettled': -1,
                                    'workerStart': -1},
                         'url': 'https://nowsecure.nl/cdn-cgi/images/trace/jschal/js/transparent.gif?ray=65444b779ae6546f'},
            'timestamp': 190011.174536,
            'type': 'Image'}}
{'method': 'Network.dataReceived',
 'params': {'dataLength': 42,
            'encodedDataLength': 0,
            'requestId': '17180.3',
            'timestamp': 190011.174737}}
{'method': 'Network.dataReceived',
 'params': {'dataLength': 0,
            'encodedDataLength': 44,
            'requestId': '17180.3',
            'timestamp': 190011.17524}}
{'method': 'Network.loadingFinished',
 'params': {'encodedDataLength': 258,
            'requestId': '17180.3',
            'shouldReportCorbBlocking': False,
            'timestamp': 190011.152073}}
{'method': 'Network.responseReceived',
 'params': {'frameId': 'F42BAE4BDD4E428EE2503CB5A7B4F700',
            'loaderId': '449906A5C736D819123288133F2797E6',
            'requestId': '17180.4',
            'response': {'connectionId': 0,
                         'connectionReused': True,
                         'encodedDataLength': 178,
                         'fromDiskCache': False,
                         'fromPrefetchCache': False,
                         'fromServiceWorker': False,
                         'headers': {'accept-ranges': 'bytes',
                                     'cache-control': 'max-age=7200\npublic',
                                     'cf-ray': '65444b781d1fe604-LHR',
                                     'content-length': '42',
                                     'content-type': 'image/gif',
                                     'date': 'Mon, 24 May 2021 05:58:53 GMT',
                                     'etag': '"60a4d856-2a"',
                                     'expires': 'Mon, 24 May 2021 07:58:53 GMT',
                                     'last-modified': 'Wed, 19 May 2021 '
                                                      '09:20:22 GMT',
                                     'server': 'cloudflare',
                                     'vary': 'Accept-Encoding',
                                     'x-content-type-options': 'nosniff',
                                     'x-frame-options': 'DENY'},
                         'mimeType': 'image/gif',
                         'protocol': 'h3-29',
                         'remoteIPAddress': '104.21.5.197',
                         'remotePort': 443,
                         'requestHeaders': {':authority': 'nowsecure.nl',
                                            ':method': 'GET',
                                            ':path': '/cdn-cgi/images/trace/jschal/nojs/transparent.gif?ray=65444b779ae6546f',
                                            ':scheme': 'https',
                                            'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
                                            'accept-encoding': 'gzip, deflate, '
                                                               'br',
                                            'accept-language': 'en-US,en;q=0.9',
                                            'referer': 'https://nowsecure.nl/',
                                            'sec-ch-ua': '" Not '
                                                         'A;Brand";v="99", '
                                                         '"Chromium";v="90", '
                                                         '"Google '
                                                         'Chrome";v="90"',
                                            'sec-ch-ua-mobile': '?0',
                                            'sec-fetch-dest': 'image',
                                            'sec-fetch-mode': 'no-cors',
                                            'sec-fetch-site': 'same-origin',
                                            'user-agent': 'Mozilla/5.0 '
                                                          '(Windows NT 10.0; '
                                                          'Win64; x64) '
                                                          'AppleWebKit/537.36 '
                                                          '(KHTML, like Gecko) '
                                                          'Chrome/90.0.4430.212 '
                                                          'Safari/537.36'},
                         'responseTime': 1621835932268.067,
                         'securityDetails': {'certificateId': 0,
                                             'certificateTransparencyCompliance': 'compliant',
                                             'cipher': 'AES_128_GCM',
                                             'issuer': 'Cloudflare Inc ECC '
                                                       'CA-3',
                                             'keyExchange': '',
                                             'keyExchangeGroup': 'X25519',
                                             'protocol': 'QUIC',
                                             'sanList': ['sni.cloudflaressl.com',
                                                         '*.nowsecure.nl',
                                                         'nowsecure.nl'],
                                             'signedCertificateTimestampList': [{'hashAlgorithm': 'SHA-256',
                                                                                 'logDescription': 'Google '
                                                                                                   "'Argon2021' "
                                                                                                   'log',
                                                                                 'logId': 'F65C942FD1773022145418083094568EE34D131933BFDF0C2F200BCC4EF164E3',
                                                                                 'origin': 'Embedded '
                                                                                           'in '
                                                                                           'certificate',
                                                                                 'signatureAlgorithm': 'ECDSA',
                                                                                 'signatureData': '30450221008A25458182A6E7F608FE1492086762A367381E94137952FFD621BA2E60F7E2F702203BCDEBCE1C544DECF0A113DE12B33E299319E6240426F38F08DFC04EF2E42825',
                                                                                 'status': 'Verified',
                                                                                 'timestamp': 1598706372839.0},
                                                                                {'hashAlgorithm': 'SHA-256',
                                                                                 'logDescription': 'DigiCert '
                                                                                                   'Yeti2021 '
                                                                                                   'Log',
                                                                                 'logId': '5CDC4392FEE6AB4544B15E9AD456E61037FBD5FA47DCA17394B25EE6F6C70ECA',
                                                                                 'origin': 'Embedded '
                                                                                           'in '
                                                                                           'certificate',
                                                                                 'signatureAlgorithm': 'ECDSA',
                                                                                 'signatureData': '3046022100A95A49C7435DBFC73406AC409062C27269E6E69F443A2213F3A085E3BCBD234A022100DEA878296F8A1DB43546DC1865A4C5AD2B90664A243AE0A3A6D4925802EE68A8',
                                                                                 'status': 'Verified',
                                                                                 'timestamp': 1598706372823.0}],
                                             'subjectName': 'sni.cloudflaressl.com',
                                             'validFrom': 1598659200,
                                             'validTo': 1630238400},
                         'securityState': 'secure',
                         'status': 200,
                         'statusText': '',
                         'timing': {'connectEnd': -1,
                                    'connectStart': -1,
                                    'dnsEnd': -1,
                                    'dnsStart': -1,
                                    'proxyEnd': -1,
                                    'proxyStart': -1,
                                    'pushEnd': 0,
                                    'pushStart': 0,
                                    'receiveHeadersEnd': 42.415,
                                    'requestTime': 190011.110341,
                                    'sendEnd': 25.713,
                                    'sendStart': 25.609,
                                    'sslEnd': -1,
                                    'sslStart': -1,
                                    'workerFetchStart': -1,
                                    'workerReady': -1,
                                    'workerRespondWithSettled': -1,
                                    'workerStart': -1},
                         'url': 'https://nowsecure.nl/cdn-cgi/images/trace/jschal/nojs/transparent.gif?ray=65444b779ae6546f'},
            'timestamp': 190011.175727,
            'type': 'Image'}}
{'method': 'Network.dataReceived',
 'params': {'dataLength': 42,
            'encodedDataLength': 0,
            'requestId': '17180.4',
            'timestamp': 190011.175856}}
{'method': 'Network.dataReceived',
 'params': {'dataLength': 0,
            'encodedDataLength': 44,
            'requestId': '17180.4',
            'timestamp': 190011.176133}}
{'method': 'Network.loadingFinished',
 'params': {'encodedDataLength': 222,
            'requestId': '17180.4',
            'shouldReportCorbBlocking': False,
            'timestamp': 190011.153335}}
{'method': 'Network.responseReceivedExtraInfo',
 'params': {'blockedCookies': [],
            'headers': {'alt-svc': 'h3-27=":443"; ma=86400, h3-28=":443"; '
                                   'ma=86400, h3-29=":443"; ma=86400',
                        'cache-control': 'max-age=0, must-revalidate',
                        'cf-ray': '65444b781d1ee604-LHR',
                        'cf-request-id': '0a3e8d7f140000e60496387000000001',
                        'content-encoding': 'br',
                        'content-type': 'text/javascript',
                        'date': 'Mon, 24 May 2021 05:58:53 GMT',
                        'expect-ct': 'max-age=604800, '
                                     'report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"',
                        'nel': '{"report_to":"cf-nel","max_age":604800}',
                        'report-to': '{"endpoints":[{"url":"https:\\/\\/a.nel.cloudflare.com\\/report?s=ZtI%2Bx8B7DpI8%2FsDA72maecFVCPvIsfBOyJjT8weyiqfmrHrmcBYpRhc%2FI%2F6JmIlnxW%2F%2BBohxLi1F8mpjAUabJ0kXLYnmjGKp2Ndio9M%3D"}],"group":"cf-nel","max_age":604800}',
                        'server': 'cloudflare',
                        'vary': 'Accept-Encoding'},
            'requestId': '17180.2',
            'resourceIPAddressSpace': 'Public'}}
{'method': 'Network.responseReceived',
 'params': {'frameId': 'F42BAE4BDD4E428EE2503CB5A7B4F700',
            'loaderId': '449906A5C736D819123288133F2797E6',
            'requestId': '17180.2',
            'response': {'connectionId': 0,
                         'connectionReused': True,
                         'encodedDataLength': 510,
                         'fromDiskCache': False,
                         'fromPrefetchCache': False,
                         'fromServiceWorker': False,
                         'headers': {'alt-svc': 'h3-27=":443"; ma=86400, '
                                                'h3-28=":443"; ma=86400, '
                                                'h3-29=":443"; ma=86400',
                                     'cache-control': 'max-age=0, '
                                                      'must-revalidate',
                                     'cf-ray': '65444b781d1ee604-LHR',
                                     'cf-request-id': '0a3e8d7f140000e60496387000000001',
                                     'content-encoding': 'br',
                                     'content-type': 'text/javascript',
                                     'date': 'Mon, 24 May 2021 05:58:53 GMT',
                                     'expect-ct': 'max-age=604800, '
                                                  'report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"',
                                     'nel': '{"report_to":"cf-nel","max_age":604800}',
                                     'report-to': '{"endpoints":[{"url":"https:\\/\\/a.nel.cloudflare.com\\/report?s=ZtI%2Bx8B7DpI8%2FsDA72maecFVCPvIsfBOyJjT8weyiqfmrHrmcBYpRhc%2FI%2F6JmIlnxW%2F%2BBohxLi1F8mpjAUabJ0kXLYnmjGKp2Ndio9M%3D"}],"group":"cf-nel","max_age":604800}',
                                     'server': 'cloudflare',
                                     'vary': 'Accept-Encoding'},
                         'mimeType': 'text/javascript',
                         'protocol': 'h3-29',
                         'remoteIPAddress': '104.21.5.197',
                         'remotePort': 443,
                         'requestHeaders': {':authority': 'nowsecure.nl',
                                            ':method': 'GET',
                                            ':path': '/cdn-cgi/challenge-platform/h/b/orchestrate/jsch/v1?ray=65444b779ae6546f',
                                            ':scheme': 'https',
                                            'accept': '*/*',
                                            'accept-encoding': 'gzip, deflate, '
                                                               'br',
                                            'accept-language': 'en-US,en;q=0.9',
                                            'referer': 'https://nowsecure.nl/',
                                            'sec-ch-ua': '" Not '
                                                         'A;Brand";v="99", '
                                                         '"Chromium";v="90", '
                                                         '"Google '
                                                         'Chrome";v="90"',
                                            'sec-ch-ua-mobile': '?0',
                                            'sec-fetch-dest': 'script',
                                            'sec-fetch-mode': 'no-cors',
                                            'sec-fetch-site': 'same-origin',
                                            'user-agent': 'Mozilla/5.0 '
                                                          '(Windows NT 10.0; '
                                                          'Win64; x64) '
                                                          'AppleWebKit/537.36 '
                                                          '(KHTML, like Gecko) '
                                                          'Chrome/90.0.4430.212 '
                                                          'Safari/537.36'},
                         'responseTime': 1621835932301.817,
                         'securityDetails': {'certificateId': 0,
                                             'certificateTransparencyCompliance': 'compliant',
                                             'cipher': 'AES_128_GCM',
                                             'issuer': 'Cloudflare Inc ECC '
                                                       'CA-3',
                                             'keyExchange': '',
                                             'keyExchangeGroup': 'X25519',
                                             'protocol': 'QUIC',
                                             'sanList': ['sni.cloudflaressl.com',
                                                         '*.nowsecure.nl',
                                                         'nowsecure.nl'],
                                             'signedCertificateTimestampList': [{'hashAlgorithm': 'SHA-256',
                                                                                 'logDescription': 'Google '
                                                                                                   "'Argon2021' "
                                                                                                   'log',
                                                                                 'logId': 'F65C942FD1773022145418083094568EE34D131933BFDF0C2F200BCC4EF164E3',
                                                                                 'origin': 'Embedded '
                                                                                           'in '
                                                                                           'certificate',
                                                                                 'signatureAlgorithm': 'ECDSA',
                                                                                 'signatureData': '30450221008A25458182A6E7F608FE1492086762A367381E94137952FFD621BA2E60F7E2F702203BCDEBCE1C544DECF0A113DE12B33E299319E6240426F38F08DFC04EF2E42825',
                                                                                 'status': 'Verified',
                                                                                 'timestamp': 1598706372839.0},
                                                                                {'hashAlgorithm': 'SHA-256',
                                                                                 'logDescription': 'DigiCert '
                                                                                                   'Yeti2021 '
                                                                                                   'Log',
                                                                                 'logId': '5CDC4392FEE6AB4544B15E9AD456E61037FBD5FA47DCA17394B25EE6F6C70ECA',
                                                                                 'origin': 'Embedded '
                                                                                           'in '
                                                                                           'certificate',
                                                                                 'signatureAlgorithm': 'ECDSA',
                                                                                 'signatureData': '3046022100A95A49C7435DBFC73406AC409062C27269E6E69F443A2213F3A085E3BCBD234A022100DEA878296F8A1DB43546DC1865A4C5AD2B90664A243AE0A3A6D4925802EE68A8',
                                                                                 'status': 'Verified',
                                                                                 'timestamp': 1598706372823.0}],
                                             'subjectName': 'sni.cloudflaressl.com',
                                             'validFrom': 1598659200,
                                             'validTo': 1630238400},
                         'securityState': 'secure',
                         'status': 200,
                         'statusText': '',
                         'timing': {'connectEnd': -1,
                                    'connectStart': -1,
                                    'dnsEnd': -1,
                                    'dnsStart': -1,
                                    'proxyEnd': -1,
                                    'proxyStart': -1,
                                    'pushEnd': 0,
                                    'pushStart': 0,
                                    'receiveHeadersEnd': 78.885,
                                    'requestTime': 190011.107975,
                                    'sendEnd': 27.934,
                                    'sendStart': 27.809,
                                    'sslEnd': -1,
                                    'sslStart': -1,
                                    'workerFetchStart': -1,
                                    'workerReady': -1,
                                    'workerRespondWithSettled': -1,
                                    'workerStart': -1},
                         'url': 'https://nowsecure.nl/cdn-cgi/challenge-platform/h/b/orchestrate/jsch/v1?ray=65444b779ae6546f'},
            'timestamp': 190011.188468,
            'type': 'Script'}}
{'method': 'Network.dataReceived',
 'params': {'dataLength': 31556,
            'encodedDataLength': 0,
            'requestId': '17180.2',
            'timestamp': 190011.188663}}
{'method': 'Network.dataReceived',
 'params': {'dataLength': 6737,
            'encodedDataLength': 11251,
            'requestId': '17180.2',
            'timestamp': 190011.198249}}
{'method': 'Network.dataReceived',
 'params': {'dataLength': 0,
            'encodedDataLength': 2049,
            'requestId': '17180.2',
            'timestamp': 190011.200943}}
{'method': 'Network.loadingFinished',
 'params': {'encodedDataLength': 13810,
            'requestId': '17180.2',
            'shouldReportCorbBlocking': False,
            'timestamp': 190011.198142}}
{'method': 'Page.loadEventFired', 'params': {'timestamp': 190011.204711}}
{'method': 'Page.frameScheduledNavigation',
 'params': {'delay': 12,
            'frameId': 'F42BAE4BDD4E428EE2503CB5A7B4F700',
            'reason': 'metaTagRefresh',
            'url': 'https://nowsecure.nl/'}}
{'method': 'Page.frameStoppedLoading',
 'params': {'frameId': 'F42BAE4BDD4E428EE2503CB5A7B4F700'}}
{'method': 'Network.requestWillBeSent',
 'params': {'documentURL': 'https://nowsecure.nl/',
            'frameId': 'F42BAE4BDD4E428EE2503CB5A7B4F700',
            'hasUserGesture': False,
            'initiator': {'type': 'other'},
            'loaderId': '449906A5C736D819123288133F2797E6',
            'request': {'headers': {'Referer': 'https://nowsecure.nl/',
                                    'User-Agent': 'Mozilla/5.0 (Windows NT '
                                                  '10.0; Win64; x64) '
                                                  'AppleWebKit/537.36 (KHTML, '
                                                  'like Gecko) '
                                                  'Chrome/90.0.4430.212 '
                                                  'Safari/537.36',
                                    'sec-ch-ua': '" Not A;Brand";v="99", '
                                                 '"Chromium";v="90", "Google '
                                                 'Chrome";v="90"',
                                    'sec-ch-ua-mobile': '?0'},
                        'initialPriority': 'High',
                        'method': 'GET',
                        'mixedContentType': 'none',
                        'referrerPolicy': 'strict-origin-when-cross-origin',
                        'url': 'https://nowsecure.nl/favicon.ico'},
            'requestId': '17180.5',
            'timestamp': 190011.210491,
            'type': 'Other',
            'wallTime': 1621835932.325683}}