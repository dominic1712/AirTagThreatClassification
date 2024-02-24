def threat_classification_tree():
    classification_tree = {
        '1.': {
            'question': '1.: What issues inside the AirTag system do you want to analyze?',
            'options': {
                '1.1': '1.1 iOS-related AirTag issues',
                '1.2': '1.2 Android-related issues',
                '1.3': '1.3 Sound-related issues',
                '1.4': '1.4 BLE-related issues',
                '1.5': '1.5 macOS-related issues',
                '1.6': '1.6 FindMy Authentication-related issues'
            }
        },
        '1.1 iOS-related AirTag issues': {
            'question': '1.1: These are all Item Safety Alert related-issues. Choose one:',
            'options': {
                '1.1.1': '1.1.1 Inadvertent Disabling of the ISA',
                '1.1.2': '1.1.2 No Manual Scanning Possibility',
                '1.1.3': '1.1.3 Low Reliability',
                '1.1.4': '1.1.4 ISA Trigger Blocking'
            }
        },
        '1.1.4 ISA Trigger Blocking': {
            'question': "1.1.4: These are the methods used for blocking the triggering of ISA's. Choose one",
            'options': {
                '1.1.4.1': '1.1.4.1 Changing of Status Bytes in the BLE advertisement',
                '1.1.4.2': '1.1.4.2 Periodic Key changing'
            }
        },
        '1.2 Android-related issues': {
            'question': "1.2: These are all issues related to Apple's "
                        "Tracker Detect App on the Google Play Store. Choose one:",
            'options': {
                '1.2.1': '1.2.1 No Background Scanning Possibility',
                '1.2.2': '1.2.2 Low Awareness and Detectability'
            }
        },
        '1.3 Sound-related issues': {
            'question': '1.3: These are all issues related to the sound played by an AirTag. Choose one:',
            'options': {
                '1.3.1': '1.3.1 No Active Triggering',
                '1.3.2': '1.3.2 Insufficient Volume Level',
                '1.3.3': '1.3.3 Non-Distinct Sound',
                '1.3.4': '1.3.4 Short Duration',
                '1.3.5': '1.3.5 Inadvertent Disabling',
                '1.3.6': '1.3.6 Delay'
            }
        },
        '1.4 BLE-related issues': {
            'question': '1.4: The following issues are BLE-related issues. Choose one:',
            'options': {
                '1.4.1': '1.4.1 RSSI-based Fingerprinting',
                '1.4.2': '1.4.2 Byte changing of BLE advertisements to block ISA from triggering',
            }
        },
        '1.5 macOS-related issues': {
            'question': '1.5: The following are issues related to macOS. Choose one:',
            'options': {
                '1.5.1': '1.5.1 Historical Location Access'
            }
        },
        '1.6 FindMy Authentication-related issues': {
            'question': '1.6: These are issues related to the FindMy Authentication process. Choose one:',
            'options': {
                '1.6.1': '1.6.1 Linking Reports to the same device',
                '1.6.2': '1.6.2 Uploading of Fake Reports through OpenHaystack',
                '1.6.3': '1.6.3 Periodic Key changing to block ISA from triggering'
            }
        },
        '1.1.1 Inadvertent Disabling of the ISA': {
            'information': 'Information: As the ISA is a pop up notification on the iPhone lockscreen, '
                           'it is possible, that the notification could be disabled by accident.'
        },
        '1.1.2 No Manual Scanning Possibility': {
            'information': 'Information: The Scanning is only conducted in the background. It can not be done manually.'
        },
        '1.1.3 Low Reliability': {
            'information': 'Information: It has been reported that, the triggering of the ISA is unreliable, '
                           'as the detection time varies and sometimes takes too long.'
        },
        '1.1.4.1 Changing of Status Bytes in the BLE advertisement': {
            'information': 'Information: If the Battery Status bytes in a BLE advertisement message from an AirTag are '
                           'altered to a to the system unknown value, the ISA will not trigger.'
        },
        '1.1.4.2 Periodic Key changing': {
            'information': 'Information: By manually changing the pseudo-random public key every few minutes, the triggering of the '
                           'ISA can be prevented, as the ISA asserts a different key in a little time span to a different device.'
        },
        '1.2.1 No Background Scanning Possibility': {
            'information': 'Information: There is no possibility of letting the App scan passively in the background.'

        },
        '1.2.2 Low Awareness and Detectability': {
            'information': "Information: The App has difficulties detecting 'stalker AirTags' and generally has low awareness especially in crowded areas."
        },
        '1.3.1 No Active Triggering': {
            'information': 'Information: The sound played by an AirTag can not be actively triggered.'
        },
        '1.3.2 Insufficient Volume Level': {
            'information': 'Information: The volume level of the sound played by the AirTag is too low.'
        },
        '1.3.3 Non-Distinct Sound': {
            'information': 'Information: The sound played by an AirTag is not distinct. '
                           'Without further knowledge it can not be conclusively determined, whether the sound is played by the AirTag or not. '
        },
        '1.3.4 Short Duration': {
            'information': 'Information: The sound played by an AirTag is too short.'
        },
        '1.3.5 Inadvertent Disabling': {
            'information': 'Information: The sound played by an AirTag can be disabled by accident.'
        },
        '1.3.6 Delay': {
            'information': 'Information: There is an unknown delay until the sound alert is triggered.'
        },
        '1.4.1 RSSI-based Fingerprinting': {
            'information': 'Information: With the RSSI values from the BLE advertisements, it is possible to link different '
                           'signals to the same device and therefore bypass the MAC Randomization protection mechanism. '
        },
        '1.4.2 Byte changing of BLE advertisements to block ISA from triggering': {
            'information': 'Information: If the Battery Status bytes in a BLE advertisement message from an AirTag are '
                           'altered to a to the system unknown value, the ISA will not trigger.'
        },
        '1.5.1 Historical Location Access': {
            'information': 'Information: By caching the advertisement keys of the past seven days on a macOS '
                           'directory, any third-party application with user priviledges is able to exploit it '
                           'to gain access to historical location data.'
        },
        '1.6.1 Linking Reports to the same device': {
            'information': 'Information: While downloading a location report, the owner device includes its '
                           'Apple ID in the HTTPS request header, which reveals personally identifying information.'
        },
        '1.6.2 Uploading of Fake Reports through OpenHaystack': {
            'information': 'Information: Tools like OpenHaystack have been successfully used to upload location reports '
                           'by fake AirTags, which act similarly to real ones.'
        },
        '1.6.3 Periodic Key changing to block ISA from triggering': {
            'information': 'Information: By manually changing the pseudo-random public key every few minutes, the '
                           'triggering of the ISA can be prevented, as the ISA asserts a different'
                           ' key in a little time span to a different device.'
        }

    }
    return classification_tree


def traverse_threat_classification_tree(tree):
    current_node = '1.'

    while True:
        if 'question' in tree[current_node]:
            print(tree[current_node]['question'])
            for option, description in tree[current_node]['options'].items():
                print(f"Type '{option}' for {description}")
            user_input = input().lower()
            if user_input in tree[current_node]['options']:
                current_node = tree[current_node]['options'][user_input]
            else:
                print("Invalid input. Please try again.")
        else:
            print(tree[current_node]['information'])
            break


def main():
    tree = threat_classification_tree()
    traverse_threat_classification_tree(tree)


if __name__ == "__main__":
    main()