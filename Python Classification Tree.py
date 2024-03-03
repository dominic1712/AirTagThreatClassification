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
                '1.3.5': '1.3.5 Simple Disabling by Speaker Removal',
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
                '1.6.1': '1.6.1 Linking the Finder Device to the Owner Device in Location Reports',
                '1.6.2': '1.6.2 Uploading of Fake Reports through OpenHaystack',
                '1.6.3': '1.6.3 Periodic Key changing to block ISA from triggering'
            }
        },
        '1.1.1 Inadvertent Disabling of the ISA': {
            'information': 'Information: As the ISA is a pop up notification on the iPhone lockscreen, '
                           'it is possible, that the notification could be disabled by accident.',
            'threat': 'Threat: It could occur, that the ISA appears on the home screen at an inconvenient time, where the user mindlessly disregards and disables it. After disabling it, it is gone and will not be triggered again.',
            'privacy requirement': '(1) Awareness'

        },
        '1.1.2 No Manual Scanning Possibility': {
            'information': 'Information: The Scanning is only conducted in the background. It can not be done manually.',
            'threat': 'Threat: If an iPhone user suspects that someone is stalking him with an AirTag, he can not actively conduct a scan of nearby suspicious AirTags using the ISA feature. He is left with the possibilities of searching for it manually, or waiting for an ISA to appear. ',
            'privacy requirement': '(1) Awareness'
        },
        '1.1.3 Low Reliability': {
            'information': 'Information: It has been reported that, the triggering of the ISA is unreliable, '
                           'as the detection time varies and sometimes takes too long.',
            'threat': 'Threat: The triggering of the ISA has been reported to take too long. For example, if someone is being stalked using an AirTag, and only receives the notification after returning home, the stalker will know where the victim lives. This can seriously endanger the life of the victim.',
            'privacy requirement': '(1) Awareness'
        },
        '1.1.4.1 Changing of Status Bytes in the BLE advertisement': {
            'information': 'Information: If the Battery Status bytes in a BLE advertisement message from an AirTag are '
                           'altered to a to the system unknown value, the ISA will not trigger.',
            'threat': 'Threat: As the ISA is the main tracker detection method for iOS users, being able to disable it entirely by changing a byte value in the BLE advertisement could be potentially very dangerous for stalker victims. The only other automatic detection method left is the sound alert feature (1.3), which has been deemed as unreliable.',
            'privacy requirement': '(1) Awareness'
        },
        '1.1.4.2 Periodic Key changing': {
            'information': 'Information: By manually changing the pseudo-random public key every few minutes, the triggering of the '
                           'ISA can be prevented, as the ISA asserts a different key in a little time span to a different device.',
            'threat': 'Threat: As the ISA is the main tracker detection method for iOS users, being able to disable it entirely by periodically changing the public key could be potentially very dangerous for stalker victims. The only other automatic detection method left is the sound alert feature (1.3), which has been deemed as unreliable.',
            'privacy requirement': '(1) Awareness'
                        
        },
        '1.2.1 No Background Scanning Possibility': {
            'information': 'Information: There is no possibility of letting the App scan passively in the background.',
            'threat': 'Threat: Without any previous incidents, a regular person is unlikely to suspect they are being stalked. Therefore, having a tracker detection application, that only runs through manual scans, is quite unreliable and useless on a daily basis. If a stalker is able to place an AirTag with an Android smartphone user without them becoming suspicious or aware of it, the only detection method left is the sound alert feature (1.3), which has been deemed as unreliable.',
            'privacy requirement': '(1) Awareness'

        },
        '1.2.2 Low Awareness and Detectability': {
            'information': "Information: The App has difficulties detecting 'stalker AirTags' and generally has low awareness especially in crowded areas.",
            'threat': "Threat: If an Android victim living inside a big city is suspicious of being stalked with an AirTag, and he conducts a manual scan using the tracker detect app, the app will show nearby Find My devices, yet will not be able to tell, which one is a stalker's AirTag. As there are many Find My devices inside large cities, many devices are shown, yet no suggestive remarks towards finding the stalker AirTag can be delivered by the app. ",
            'privacy requirement': '(1) Awareness'
        },
        '1.3.1 No Active Triggering': {
            'information': 'Information: The sound played by an AirTag can not be actively triggered.',
            'threat': "Threat: If a victim is actively searching for a stalker's AirTag, he is unable to proactively trigger the sound alert, which could simplify the search process. Because of this, he may not find the AirTag at all, which could lead to continuous tracking by the stalker.",
            'privacy requirement': '(1) Awareness'
        },
        '1.3.2 Insufficient Volume Level': {
            'information': 'Information: The volume level of the sound played by the AirTag is too low.',
            'threat': 'Threat: If the sound played by the AirTag is muffled, the user is unable to hear the sound which makes the search process much more difficult. Because of this, he may not find the AirTag at all, which could lead to continuous tracking by the stalker.',
            'privacy requirement': '(1) Awareness'
        },
        '1.3.3 Non-Distinct Sound': {
            'information': 'Information: The sound played by an AirTag is not distinct. '
                           'Without further knowledge it can not be conclusively determined, whether the sound is played by the AirTag or not. ',
            'threat': 'Threat: The sound could be mistaken for a sound played by another device. Therefore, he might not take action to find out where the sound came from which could lead to continuous stalking.',
            'privacy requirement': '(1) Awareness'
        },
        '1.3.4 Short Duration': {
            'information': 'Information: The sound played by an AirTag is too short.',
            'threat': 'Threat: The duration of the sound alert being too short could lead to the user looking for it while the sound is playing, yet not being able to find it in that time. When the auditory aid is gone, it becomes increasingly difficult to find the AirTag. ',
            'privacy requirement': '(1) Awareness'
        },
        '1.3.5 Simple Disabling by Speaker Removal': {
            'information': 'Information: The sound alert feature can be bygone by removing the speaker from the AirTag. The AirTag remains functional',
            'threat': "Threat: By removing a detection mechanism, stalking with AirTags is facilitated from a stalker's perspective and has a higher chance of being undetected by the victim. This concerns especially non-smartphone victims, whose only stalking detection method is the sound-alert feature. ",
            'privacy requirement': '(1) Awareness'
        },
        '1.3.6 Delay': {
            'information': 'Information: There is an unknown delay until the sound alert is triggered.',
            'threat': "Threat: If a victim is unknowingly carrying a stalker's AirTag with him, a delay of the sound alert feature could lead to the victim only being aware of the stalking after he reaches his home. By that time, the stalker already has gathered enough information to continously stalk the victim. ",
            'privacy requirement': '(1) Awareness'
        },
        '1.4.1 RSSI-based Fingerprinting': {
            'information': 'Information: With the RSSI values from the BLE advertisements, it is possible to link different '
                           'signals to the same device and therefore bypass the MAC Randomization protection mechanism. ',
            'threat': 'Threat: By gaining enough data, a user can pinpoint an AirTag out of a set of AirTags around him. Therefore, it is possible to track the same AirTag for an extensive amount of time.',
            'privacy requirement': '(9) Anonymity, (10) Unlinkability'
        },
        '1.4.2 Byte changing of BLE advertisements to block ISA from triggering': {
            'information': 'Information: If the Battery Status bytes in a BLE advertisement message from an AirTag are '
                           'altered to a to the system unknown value, the ISA will not trigger.',
            'threat': 'Threat: As the ISA is the main tracker detection method for iOS users, being able to disable it entirely by changing a byte value in the BLE advertisement could be potentially very dangerous for stalker victims. The only other automatic detection method left is the sound alert feature (1.3), which has been deemed as unreliable.',
            'privacy requirement': '(1) Awareness'
        },
        '1.5.1 Historical Location Access': {
            'information': 'Information: By caching the advertisement keys of the past seven days on a macOS '
                           'directory, any third-party application with user priviledges is able to exploit it '
                           'to gain access to historical location data.',
            'threat': 'Threat: A third-party application can disguise itself as a system-relevant application, for which user priviledges are necessary. If the user grants these priviledges, the system can access the cached keys, which in turn can be used to gain historical location data.',
            'privacy requirement': '(3) Confidentiality'
        },
        '1.6.1 Linking the Finder Device to the Owner Device in Location Reports': {
            'information': 'Information: While downloading a location report, the owner device includes its '
                           'Apple ID in the HTTPS request header, which reveals personally identifying information. Similarly, when a finder device uploads a location report, ' 
                           'it also includes its Apple ID in the HTTPS request header. ',
            'threat': 'Threat: Apple could link the finder and owner devices of several location reports, to map, which devices have been near each other. ',
            'privacy requirement': '(9) Anonymity, (10) Unlinkability'
        },
        '1.6.2 Uploading of Fake Reports through OpenHaystack': {
            'information': 'Information: Tools like OpenHaystack have been successfully used to upload location reports '
                           'by fake AirTags, which act similarly to real ones.',
            'threat': 'Threat: Through fake location reports, imprecise location reports can be created which could be exploited to reduce the accuracy of the downloadable owner location reports. ',
            'privacy requiremennt': '(6) Accuracy'
        },
        '1.6.3 Periodic Key changing to block ISA from triggering': {
            'information': 'Information: By manually changing the pseudo-random public key every few minutes, the '
                           'triggering of the ISA can be prevented, as the ISA asserts a different'
                           ' key in a little time span to a different device.',
            'threat': 'Threat: As the ISA is the main tracker detection method for iOS users, being able to disable it entirely by periodically changing the public key could be potentially very dangerous for stalker victims. The only other automatic detection method left is the sound alert feature (1.3), which has been deemed as unreliable.',
            'privacy requirement': '(1) Awareness'
        }

    }
    return classification_tree

intro_text = print("""----------------------------------------------------------------------------------------------------------------------------------------------------------------
Welcome to the AirTag Classification Tree
----------------------------------------------------------------------------------------------------------------------------------------------------------------            
This Tree was designed to exploratively analyze current AirTag-related threats. 
For each threat, there are three parts:
    -An information: How to achieve the threat?
    -Threat: What makes it a threat?
    -Privacy Requirement: What privacy requirements does the threat breach?
                   
Following is a short summary of all privacy requirements:
                   
    (1) Awareness: The Data Subject is aware, that his/her personal data is being collected and processed.
    (2) Transparency: The Data Subject is aware of the specific purposes for which the data is being processed.
    (3) Confidentiality: Personal information is stored with appropriate security measures.
    (4) Accountability: The Data Subject can hold the controllers for their actions accountable.
    (5) Data Minimization: The personal data acquired is kept to a bare minimum and proportionate.
    (6) Accuracy: The personal data stored must be accurate and correct.
    (7) Storage Limitation: The data may only be stored for as long as necessary.
    (8) Lawfulness: The data is lawfully processed.
    (9) Anonymity: Personal data should limit the possible identification of the subject.
    (10) Unlinkability: It should be impossible to connect personal information back to the data subject.
    (11) Unobservability: The use of services by the data subject is not visible to third parties.
    (12) Good Faith: Personal Data must be processed in good faith.
    (13) Access and Correction: The Data Subject should be able to obtain their personal information collected about them.
    (14) Choice: The Data Subject should be able to exercise chose to the collection, use and disclosure of their personal information. 

The classification tree can be walked through by typing in the numbers of the threat that wants to be analyzed deeper.        
                    """)
                

def traverse_threat_classification_tree(tree):
    current_node = '1.'
    history = []
    while True:
        print("")
        if 'question' in tree[current_node]:
            print(tree[current_node]['question'])
            for option, description in tree[current_node]['options'].items():
                print(f"Type '{option}' for {description}")
            user_input = input("Enter here: ").lower()
            if user_input in tree[current_node]['options']:
                current_node = tree[current_node]['options'][user_input]
            else:
                print("Invalid input. Please try again.")
        else:
            print(tree[current_node]['information'])
            print(tree[current_node]['threat'])
            if len(tree[current_node]['privacy requirement'].split(" ")) > 2:
                print("The following privacy requirements are threatened: " + tree[current_node]['privacy requirement'])
            else:
                print("The following privacy requirement is threatened: " + tree[current_node]['privacy requirement'])
            print("")
            if tree[current_node] not in history: 
                history.append(tree[current_node])
            user_input = input("This threat has been added to your current set of threats you analyzed. Do you want to rerun the classification tree? (yes/no)\n").lower()
            if user_input == "no":
                print("End of Threat Analysis\n")
                return history
            else:
                current_node = '1.'
    

def main():
    print(intro_text)
    tree = threat_classification_tree()
    history = traverse_threat_classification_tree(tree)
    print("Following is a set of threats you've analyzed")
    for threat in history:
        print("\n")
        print(threat['information'])
        print(threat['threat'])
        print(threat['privacy requirement'])
        print("\n")

if __name__ == "__main__":
    main()