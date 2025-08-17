# 17101318 - Runic Seal

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Caedarva Mire (ID: 79) |
| Block Size       | 912 bytes              |
| Total Events     | 3                      |
| References Count | 29                     |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [130](#event-130)     | 0x0001       |    110 |             19 |
| [140](#event-140)     | 0x006F       |    654 |            123 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x021C      |         540 |
|       1 | 0x0001      |           1 |
|       2 | 0x00C9      |         201 |
|       3 | 0x0000      |           0 |
|       4 | 0x003C      |          60 |
|       5 | 0x001E      |          30 |
|       6 | 0x40000000  |  1073741824 |
|       7 | 0x1D46      |        7494 |
|       8 | 0x0002      |           2 |
|       9 | 0x0003      |           3 |
|      10 | 0x1D47      |        7495 |
|      11 | 0x0004      |           4 |
|      12 | 0x0006      |           6 |
|      13 | 0x0012      |          18 |
|      14 | 0x0015      |          21 |
|      15 | 0x1D2A      |        7466 |
|      16 | 0x1D2B      |        7467 |
|      17 | 0x0007      |           7 |
|      18 | 0x031D      |         797 |
|      19 | 0x1D3D      |        7485 |
|      20 | 0x1D2C      |        7468 |
|      21 | 0x1D2E      |        7470 |
|      22 | 0x1D2F      |        7471 |
|      23 | 0x1D30      |        7472 |
|      24 | 0x1D31      |        7473 |
|      25 | 0x1D32      |        7474 |
|      26 | 0x1D39      |        7481 |
|      27 | 0x1D33      |        7475 |
|      28 | 0x1D34      |        7476 |

## String References

- **7466**: The suggested level for $0 is $3. Place a level restriction on the party?
- **7467**: Place a level restriction? [No./Level 70./Level 60./Level 50.]
- **7468**: Your party's level will be [unrestricted/restricted to 70/restricted to 60/restricted to 50] for "$0."
- **7470**: Accept this setting? [Yes./No.]
- **7471**: Only nearby party members with the same objective will accompany you to [Leujaoam Sanctum/the Mamool Ja Training Grounds/Lebros Cavern/Periqia/Ilrusi Atoll/Nyzul Isle/The Ashu Talif/Zhayolm Remnants/Arrapago Remnants/Bhaflau Remnants/Silver Sea Remnants].
- **7472**: Please confirm that all party members are cleared to enter [Leujaoam Sanctum/the Mamool Ja Training Grounds/Lebros Cavern/Periqia/Ilrusi Atoll/Nyzul Isle/The Ashu Talif/Zhayolm Remnants/Arrapago Remnants/Bhaflau Remnants/Silver Sea Remnants].
- **7473**: All party members with the appropriate clearance will now be transported to [Leujaoam Sanctum/the Mamool Ja Training Grounds/Lebros Cavern/Periqia/Ilrusi Atoll/Nyzul Isle/The Ashu Talif/Zhayolm Remnants/Arrapago Remnants/Bhaflau Remnants/Silver Sea Remnants]. Are you ready?
- **7474**: Are you ready? [Yes./No.]
- **7475**: Commencing transport to [Leujaoam Sanctum/the Mamool Ja Training Grounds/Lebros Cavern/Periqia/Ilrusi Atoll/Nyzul Isle/The Ashu Talif/Zhayolm Remnants/Arrapago Remnants/Bhaflau Remnants/Silver Sea Remnants]!
- **7476**: Entry into [Leujaoam Sanctum/the Mamool Ja Training Grounds/Lebros Cavern/Periqia/Ilrusi Atoll/Nyzul Isle/The Ashu Talif/Zhayolm Remnants/Arrapago Remnants/Bhaflau Remnants/Silver Sea Remnants] has been suspended.
- **7481**: Connecting to server. Please wait.
- **7485**: You are not in possession of $6. Unable to enter area.

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 00                                                .               
```

#### Opcodes

```
  0: 0x0000 [0x00] END_REQSTACK()
```

### Event 130

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 110 bytes |
| Instructions | 19        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    43 00 43 01 20 01 42  2D F8 FF FF 7F F8 FF FF   C.C. .B-.......
0010: 7F 32 70 63 32 1C 00 80  29 01 F0 FF FF 7F 03 03  .2pc2...).......
0020: 01 10 01 80 45 02 80 F0  FF FF 7F F0 FF FF 7F 77  ....E..........w
0030: 68 6F 31 03 80 1C 04 80  2D F8 FF FF 7F F8 FF FF  ho1.....-.......
0040: 7F 32 70 63 6B 1C 05 80  2D F8 FF FF 7F F8 FF FF  .2pck...-.......
0050: 7F 32 70 63 31 1C 05 80  45 02 80 F0 FF FF 7F F0  .2pc1...E.......
0060: FF FF 7F 77 68 69 31 03  80 46 00 20 00 21 00     ...whi1..F. .!. 
```

#### Opcodes

```
  0: 0x0001 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  1: 0x0003 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  2: 0x0005 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  3: 0x0007 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  4: 0x0008 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "2pc2" with entities [EventEntity, EventEntity]
  5: 0x0015 [0x1C] WAIT(540* ticks)
  6: 0x0018 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x03)
  7: 0x001F [0x03] Work_Zone[1] = 1*
  8: 0x0024 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
  9: 0x0035 [0x1C] WAIT(60* ticks)
 10: 0x0038 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "2pck" with entities [EventEntity, EventEntity]
 11: 0x0045 [0x1C] WAIT(30* ticks)
 12: 0x0048 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "2pc1" with entities [EventEntity, EventEntity]
 13: 0x0055 [0x1C] WAIT(30* ticks)
 14: 0x0058 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 15: 0x0069 [0x46] CAMERA_CONTROL: Restore default settings
 16: 0x006B [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 17: 0x006D [0x21] END_EVENT
 18: 0x006E [0x00] END_REQSTACK()
```

### Event 140

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x006F    |
| Data Size    | 654 bytes |
| Instructions | 123       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                               42                 B
0070: 03 01 00 06 10 03 04 00  08 10 03 01 10 06 80 02  ................
0080: 03 80 03 80 00 8F 00 03  02 00 07 80 01 DF 00 02  ................
0090: 03 80 01 80 00 9F 00 03  02 00 07 80 01 DF 00 02  ................
00A0: 03 80 08 80 00 AF 00 03  02 00 07 80 01 DF 00 02  ................
00B0: 03 80 09 80 00 BF 00 03  02 00 0A 80 01 DF 00 02  ................
00C0: 03 80 0B 80 00 CF 00 03  02 00 07 80 01 DF 00 02  ................
00D0: 03 80 0C 80 00 DF 00 03  02 00 0A 80 01 DF 00 24  ...............$
00E0: 02 00 01 80 03 10 25 02  00 10 03 80 80 F2 00 01  ......%.........
00F0: F2 00 02 00 10 03 80 02  FB 02 03 01 10 03 80 40  ...............@
0100: 0D 80 0E 80 01 10 00 10  03 01 17 00 10 02 01 17  ................
0110: 01 80 00 78 01 02 07 10  03 80 01 66 01 48 0F 80  ...x.......f.H..
0120: 23 24 10 80 03 80 03 80  25 02 00 10 03 80 00 34  #$......%......4
0130: 01 01 55 01 02 00 10 01  80 00 3F 01 01 55 01 02  ..U.......?..U..
0140: 00 10 08 80 00 4A 01 01  55 01 02 00 10 09 80 00  .....J..U.......
0150: 55 01 01 55 01 40 03 80  11 80 01 10 00 10 03 00  U..U.@..........
0160: 17 00 10 01 75 01 03 02  10 12 80 48 13 80 03 01  ....u......H....
0170: 10 06 80 21 00 01 7B 01  01 8F 01 48 14 80 23 24  ...!..{....H..#$
0180: 15 80 01 80 03 80 25 02  00 10 03 80 00 E7 02 48  ......%........H
0190: 16 80 23 48 17 80 23 48  18 80 23 24 19 80 01 80  ..#H..#H..#$....
01A0: 03 80 25 02 00 10 03 80  00 D0 02 48 1A 80 A7 00  ..%........H....
01B0: A7 01 00 00 03 01 10 03  80 40 03 80 09 80 01 10  .........@......
01C0: 00 00 02 00 00 0B 80 00  CD 02 03 06 10 01 00 48  ...............H
01D0: 1B 80 02 03 80 03 80 00  39 02 2D F8 FF FF 7F F8  ........9.-.....
01E0: FF FF 7F 32 70 63 32 1C  00 80 29 01 F0 FF FF 7F  ...2pc2...).....
01F0: 03 45 02 80 F0 FF FF 7F  F0 FF FF 7F 77 68 6F 31  .E..........who1
0200: 03 80 1C 04 80 2D F8 FF  FF 7F F8 FF FF 7F 32 70  .....-........2p
0210: 63 6B 1C 05 80 2D F8 FF  FF 7F F8 FF FF 7F 32 70  ck...-........2p
0220: 63 31 1C 05 80 45 02 80  F0 FF FF 7F F0 FF FF 7F  c1...E..........
0230: 77 68 69 31 03 80 01 CC  02 02 03 80 01 80 00 44  whi1...........D
0240: 02 01 CC 02 02 03 80 08  80 00 4F 02 01 CC 02 02  ..........O.....
0250: 03 80 09 80 00 B6 02 2D  F8 FF FF 7F F8 FF FF 7F  .......-........
0260: 32 70 62 32 1C 00 80 29  01 F0 FF FF 7F 03 45 02  2pb2...)......E.
0270: 80 F0 FF FF 7F F0 FF FF  7F 77 68 6F 31 03 80 1C  .........who1...
0280: 04 80 2D F8 FF FF 7F F8  FF FF 7F 32 70 62 6B 1C  ..-........2pbk.
0290: 05 80 2D F8 FF FF 7F F8  FF FF 7F 32 70 62 31 1C  ..-........2pb1.
02A0: 05 80 45 02 80 F0 FF FF  7F F0 FF FF 7F 77 68 69  ..E..........whi
02B0: 31 03 80 01 CC 02 02 03  80 0B 80 00 C1 02 01 CC  1...............
02C0: 02 02 03 80 0C 80 00 CC  02 01 CC 02 30 01 E4 02  ............0...
02D0: 02 00 10 01 80 00 E4 02  48 1C 80 23 03 01 10 06  ........H..#....
02E0: 80 01 E4 02 01 FB 02 02  00 10 01 80 00 FB 02 48  ...............H
02F0: 1C 80 23 03 01 10 06 80  01 FB 02 21 00           ..#........!.   
```

#### Opcodes

```
  0: 0x006F [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0070 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[6]
  2: 0x0075 [0x03] ExtData[1]->WorkLocal[4] = Work_Zone[8]
  3: 0x007A [0x03] Work_Zone[1] = 1073741824*
  4: 0x007F [0x02] IF !(0* == 0*) GOTO 0x008F
  5: 0x0087 [0x03] ExtData[1]->WorkLocal[2] = 7494*
  6: 0x008C [0x01] GOTO 0x00DF
  7: 0x008F [0x02] IF !(0* == 1*) GOTO 0x009F
  8: 0x0097 [0x03] ExtData[1]->WorkLocal[2] = 7494*
  9: 0x009C [0x01] GOTO 0x00DF
 10: 0x009F [0x02] IF !(0* == 2*) GOTO 0x00AF
 11: 0x00A7 [0x03] ExtData[1]->WorkLocal[2] = 7494*
 12: 0x00AC [0x01] GOTO 0x00DF
 13: 0x00AF [0x02] IF !(0* == 3*) GOTO 0x00BF
 14: 0x00B7 [0x03] ExtData[1]->WorkLocal[2] = 7495*
 15: 0x00BC [0x01] GOTO 0x00DF
 16: 0x00BF [0x02] IF !(0* == 4*) GOTO 0x00CF
 17: 0x00C7 [0x03] ExtData[1]->WorkLocal[2] = 7494*
 18: 0x00CC [0x01] GOTO 0x00DF
 19: 0x00CF [0x02] IF !(0* == 6*) GOTO 0x00DF
 20: 0x00D7 [0x03] ExtData[1]->WorkLocal[2] = 7495*
 21: 0x00DC [0x01] GOTO 0x00DF

SUBROUTINE_00DF:
 22: 0x00DF [0x24] CREATE_DIALOG(message_id=ExtData[1]->WorkLocal[2], default_option=1*, option_flags=Work_Zone[3])
 23: 0x00E6 [0x25] WAIT_DIALOG_SELECT()
 24: 0x00E7 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00F2
 25: 0x00EF [0x01] GOTO 0x00F2

SUBROUTINE_00F2:
 26: 0x00F2 [0x02] IF !(Work_Zone[0] <= 0*) GOTO 0x02FB
 27: 0x00FA [0x03] Work_Zone[1] = 0*
 28: 0x00FF [0x40] SET_BIT_WORK_RANGE(start_bit=18*, end_bit=21*, target=Work_Zone[1], source=Work_Zone[0])
 29: 0x0108 [0x03] Work_Zone_1700[1] = Work_Zone[0]
 30: 0x010D [0x02] IF !(Work_Zone_1700[1] == 1*) GOTO 0x0178
 31: 0x0115 [0x02] IF !(Work_Zone[7] == 0*) GOTO 0x0166
 32: 0x011D [0x48] [System] [7466*]:
    → "The suggested level for $0 is $3. Place a level restriction on the party?"
 33: 0x0120 [0x23] WAIT_FOR_DIALOG_INTERACTION
 34: 0x0121 [0x24] CREATE_DIALOG(message_id=7467*, default_option=0*, option_flags=0*)
    → "Place a level restriction? [No./Level 70./Level 60./Level 50.]"
 35: 0x0128 [0x25] WAIT_DIALOG_SELECT()
 36: 0x0129 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0134
 37: 0x0131 [0x01] GOTO 0x0155
 38: 0x0134 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x013F
 39: 0x013C [0x01] GOTO 0x0155
 40: 0x013F [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x014A
 41: 0x0147 [0x01] GOTO 0x0155
 42: 0x014A [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0155
 43: 0x0152 [0x01] GOTO 0x0155

SUBROUTINE_0155:
 44: 0x0155 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=7*, target=Work_Zone[1], source=Work_Zone[0])
 45: 0x015E [0x03] Work_Zone_1700[0] = Work_Zone[0]
 46: 0x0163 [0x01] GOTO 0x0175
 47: 0x0166 [0x03] Work_Zone[2] = 797*
 48: 0x016B [0x48] [System] [7485*]:
    → "You are not in possession of $6. Unable to enter area."
 49: 0x016E [0x03] Work_Zone[1] = 1073741824*
 50: 0x0173 [0x21] END_EVENT
 51: 0x0174 [0x00] END_REQSTACK()

SUBROUTINE_0175:
 52: 0x0175 [0x01] GOTO 0x017B
 53: 0x0178 [0x01] GOTO 0x018F

SUBROUTINE_017B:
 54: 0x017B [0x48] [System] [7468*]:
    → "Your party's level will be [unrestricted/restricted to 70/restricted to 60/restricted to 50] for "$0.""
 55: 0x017E [0x23] WAIT_FOR_DIALOG_INTERACTION
 56: 0x017F [0x24] CREATE_DIALOG(message_id=7470*, default_option=1*, option_flags=0*)
    → "Accept this setting? [Yes./No.]"
 57: 0x0186 [0x25] WAIT_DIALOG_SELECT()
 58: 0x0187 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x02E7

SUBROUTINE_018F:
 59: 0x018F [0x48] [System] [7471*]:
    → "Only nearby party members with the same objective will accompany you to [Leujaoam Sanctum/the Mamool Ja Training Grounds/Lebros Cavern/Periqia/Ilrusi Atoll/Nyzul Isle/The Ashu Talif/Zhayolm Remnants/Arrapago Remnants/Bhaflau Remnants/Silver Sea Remnants]."
 60: 0x0192 [0x23] WAIT_FOR_DIALOG_INTERACTION
 61: 0x0193 [0x48] [System] [7472*]:
    → "Please confirm that all party members are cleared to enter [Leujaoam Sanctum/the Mamool Ja Training Grounds/Lebros Cavern/Periqia/Ilrusi Atoll/Nyzul Isle/The Ashu Talif/Zhayolm Remnants/Arrapago Remnants/Bhaflau Remnants/Silver Sea Remnants]."
 62: 0x0196 [0x23] WAIT_FOR_DIALOG_INTERACTION
 63: 0x0197 [0x48] [System] [7473*]:
    → "All party members with the appropriate clearance will now be transported to [Leujaoam Sanctum/the Mamool Ja Training Grounds/Lebros Cavern/Periqia/Ilrusi Atoll/Nyzul Isle/The Ashu Talif/Zhayolm Remnants/Arrapago Remnants/Bhaflau Remnants/Silver Sea Remnants]. Are you ready?"
 64: 0x019A [0x23] WAIT_FOR_DIALOG_INTERACTION
 65: 0x019B [0x24] CREATE_DIALOG(message_id=7474*, default_option=1*, option_flags=0*)
    → "Are you ready? [Yes./No.]"
 66: 0x01A2 [0x25] WAIT_DIALOG_SELECT()
 67: 0x01A3 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x02D0
 68: 0x01AB [0x48] [System] [7481*]:
    → "Connecting to server. Please wait."
 69: 0x01AE [0xA7] BATTLEFIELD_RESPONSE_WAIT: Wait for server response (Dynamis/MMM/Salvage), mode=0x00
 70: 0x01B0 [0xA7] BATTLEFIELD_RESPONSE_WAIT: Wait for server response with parameter (Dynamis/MMM/Salvage), param=ExtData[1]->WorkLocal[0]
 71: 0x01B4 [0x03] Work_Zone[1] = 0*
 72: 0x01B9 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=3*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[0])
 73: 0x01C2 [0x02] IF !(ExtData[1]->WorkLocal[0] == 4*) GOTO 0x02CD
 74: 0x01CA [0x03] Work_Zone[6] = ExtData[1]->WorkLocal[1]
 75: 0x01CF [0x48] [System] [7475*]:
    → "Commencing transport to [Leujaoam Sanctum/the Mamool Ja Training Grounds/Lebros Cavern/Periqia/Ilrusi Atoll/Nyzul Isle/The Ashu Talif/Zhayolm Remnants/Arrapago Remnants/Bhaflau Remnants/Silver Sea Remnants]!"
 76: 0x01D2 [0x02] IF !(0* == 0*) GOTO 0x0239
 77: 0x01DA [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "2pc2" with entities [EventEntity, EventEntity]
 78: 0x01E7 [0x1C] WAIT(540* ticks)
 79: 0x01EA [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x03)
 80: 0x01F1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 81: 0x0202 [0x1C] WAIT(60* ticks)
 82: 0x0205 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "2pck" with entities [EventEntity, EventEntity]
 83: 0x0212 [0x1C] WAIT(30* ticks)
 84: 0x0215 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "2pc1" with entities [EventEntity, EventEntity]
 85: 0x0222 [0x1C] WAIT(30* ticks)
 86: 0x0225 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 87: 0x0236 [0x01] GOTO 0x02CC
 88: 0x0239 [0x02] IF !(0* == 1*) GOTO 0x0244
 89: 0x0241 [0x01] GOTO 0x02CC
 90: 0x0244 [0x02] IF !(0* == 2*) GOTO 0x024F
 91: 0x024C [0x01] GOTO 0x02CC
 92: 0x024F [0x02] IF !(0* == 3*) GOTO 0x02B6
 93: 0x0257 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "2pb2" with entities [EventEntity, EventEntity]
 94: 0x0264 [0x1C] WAIT(540* ticks)
 95: 0x0267 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x03)
 96: 0x026E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 97: 0x027F [0x1C] WAIT(60* ticks)
 98: 0x0282 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "2pbk" with entities [EventEntity, EventEntity]
 99: 0x028F [0x1C] WAIT(30* ticks)
100: 0x0292 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "2pb1" with entities [EventEntity, EventEntity]
101: 0x029F [0x1C] WAIT(30* ticks)
102: 0x02A2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
103: 0x02B3 [0x01] GOTO 0x02CC
104: 0x02B6 [0x02] IF !(0* == 4*) GOTO 0x02C1
105: 0x02BE [0x01] GOTO 0x02CC
106: 0x02C1 [0x02] IF !(0* == 6*) GOTO 0x02CC
107: 0x02C9 [0x01] GOTO 0x02CC

SUBROUTINE_02CC:
108: 0x02CC [0x30] SET_UCOFF_CONTINUE_ZERO()
109: 0x02CD [0x01] GOTO 0x02E4
110: 0x02D0 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x02E4
111: 0x02D8 [0x48] [System] [7476*]:
    → "Entry into [Leujaoam Sanctum/the Mamool Ja Training Grounds/Lebros Cavern/Periqia/Ilrusi Atoll/Nyzul Isle/The Ashu Talif/Zhayolm Remnants/Arrapago Remnants/Bhaflau Remnants/Silver Sea Remnants] has been suspended."
112: 0x02DB [0x23] WAIT_FOR_DIALOG_INTERACTION
113: 0x02DC [0x03] Work_Zone[1] = 1073741824*
114: 0x02E1 [0x01] GOTO 0x02E4

SUBROUTINE_02E4:
115: 0x02E4 [0x01] GOTO 0x02FB
116: 0x02E7 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x02FB
117: 0x02EF [0x48] [System] [7476*]:
    → "Entry into [Leujaoam Sanctum/the Mamool Ja Training Grounds/Lebros Cavern/Periqia/Ilrusi Atoll/Nyzul Isle/The Ashu Talif/Zhayolm Remnants/Arrapago Remnants/Bhaflau Remnants/Silver Sea Remnants] has been suspended."
118: 0x02F2 [0x23] WAIT_FOR_DIALOG_INTERACTION
119: 0x02F3 [0x03] Work_Zone[1] = 1073741824*
120: 0x02F8 [0x01] GOTO 0x02FB

SUBROUTINE_02FB:
121: 0x02FB [0x21] END_EVENT
122: 0x02FC [0x00] END_REQSTACK()
```
