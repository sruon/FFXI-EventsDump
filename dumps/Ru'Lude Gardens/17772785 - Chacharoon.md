# 17772785 - Chacharoon

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Ru'Lude Gardens (ID: 243) |
| Block Size       | 676 bytes                 |
| Total Events     | 5                         |
| References Count | 15                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [10287](#event-10287) | 0x0001       |     55 |             15 |
| [10288](#event-10288) | 0x0038       |     49 |             11 |
| [10289](#event-10289) | 0x0069       |     29 |              9 |
| [10290](#event-10290) | 0x0086       |    444 |             85 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0DEE      |        3566 |
|       1 | 0x3E8D      |       16013 |
|       2 | 0x3E93      |       16019 |
|       3 | 0x3E94      |       16020 |
|       4 | 0x3E95      |       16021 |
|       5 | 0x3E96      |       16022 |
|       6 | 0x3E98      |       16024 |
|       7 | 0x3E8E      |       16014 |
|       8 | 0x0000      |           0 |
|       9 | 0x0001      |           1 |
|      10 | 0x3E8F      |       16015 |
|      11 | 0x3E90      |       16016 |
|      12 | 0x3E91      |       16017 |
|      13 | 0x3E92      |       16018 |
|      14 | 0x0002      |           2 |

## String References

- **16013**: Happy Happy New Year!
- **16014**: Chacharoon wishing you very best in New Year the Qiqirn way--by giving you things for $5 jingly!
- **16016**: @Buy $6 for $5 gil? [Yes./No.]
- **16017**: Ooooh, $6! What is inside? Maybe you get something special!
- **16018**: Not enough jingly? Then you go out, get more jingly, and bring back. Deal?
- **16019**: In homeland, people put jingly in pouches and give to other people they like!
- **16020**: You give me jingly, I put in pouch. Then I give you pouch for you to give to friends. Okay?
- **16021**: But you cannot open pouch yourself. Only friend can. Must be Mysterious Moogle Magic.
- **16022**: Pouch with jingly! Can use to see how much is inside!
- **16024**: Oooh, listen to the happy sound of jingly! But is too much jingly for one pouch. Only up to $0 jingly.

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

### Event 10287

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 55 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  5B 00 80 F1 30 0F 01 F1   .....op[...0...
0010: 30 0F 01 74 6C 6B 30 1D  01 80 23 1D 02 80 23 1D  0..tlk0...#...#.
0020: 03 80 23 1D 04 80 23 5B  00 80 F1 30 0F 01 F1 30  ..#...#[...0...0
0030: 0F 01 74 6C 6B 31 21 00                           ..tlk1!.        
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Chacharoon (ID: 17772785/0x010F30F1), Chacharoon (ID: 17772785/0x010F30F1)], work=3566*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=16013*)
    → "Happy Happy New Year!"
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x1D] PRINT_EVENT_MESSAGE(message_id=16019*)
    → "In homeland, people put jingly in pouches and give to other people they like!"
  7: 0x001E [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x001F [0x1D] PRINT_EVENT_MESSAGE(message_id=16020*)
    → "You give me jingly, I put in pouch. Then I give you pouch for you to give to friends. Okay?"
  9: 0x0022 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0023 [0x1D] PRINT_EVENT_MESSAGE(message_id=16021*)
    → "But you cannot open pouch yourself. Only friend can. Must be Mysterious Moogle Magic."
 11: 0x0026 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0027 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [Chacharoon (ID: 17772785/0x010F30F1), Chacharoon (ID: 17772785/0x010F30F1)], work=3566*
 13: 0x0036 [0x21] END_EVENT
 14: 0x0037 [0x00] END_REQSTACK()
```

### Event 10288

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0038   |
| Data Size    | 49 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                          42 1E F0 FF FF 7F 6F 70          B.....op
0040: 5B 00 80 F1 30 0F 01 F1  30 0F 01 74 6C 6B 30 1D  [...0...0..tlk0.
0050: 05 80 23 5B 00 80 F1 30  0F 01 F1 30 0F 01 74 6C  ..#[...0...0..tl
0060: 6B 31 03 01 10 02 10 21  00                       k1.....!.       
```

#### Opcodes

```
  0: 0x0038 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0039 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x003E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x003F [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0040 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Chacharoon (ID: 17772785/0x010F30F1), Chacharoon (ID: 17772785/0x010F30F1)], work=3566*
  5: 0x004F [0x1D] PRINT_EVENT_MESSAGE(message_id=16022*)
    → "Pouch with jingly! Can use to see how much is inside!"
  6: 0x0052 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0053 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [Chacharoon (ID: 17772785/0x010F30F1), Chacharoon (ID: 17772785/0x010F30F1)], work=3566*
  8: 0x0062 [0x03] Work_Zone[1] = Work_Zone[2]
  9: 0x0067 [0x21] END_EVENT
 10: 0x0068 [0x00] END_REQSTACK()
```

### Event 10289

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0069   |
| Data Size    | 29 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             42 1E F0 FF FF 7F 6F           B.....o
0070: 70 5B 00 80 F1 30 0F 01  F1 30 0F 01 62 69 6B 30  p[...0...0..bik0
0080: 1D 06 80 23 21 00                                 ...#!.          
```

#### Opcodes

```
  0: 0x0069 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x006A [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x006F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0070 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0071 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "bik0" with entities [Chacharoon (ID: 17772785/0x010F30F1), Chacharoon (ID: 17772785/0x010F30F1)], work=3566*
  5: 0x0080 [0x1D] PRINT_EVENT_MESSAGE(message_id=16024*)
    → "Oooh, listen to the happy sound of jingly! But is too much jingly for one pouch. Only up to $0 jingly."
  6: 0x0083 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0084 [0x21] END_EVENT
  8: 0x0085 [0x00] END_REQSTACK()
```

### Event 10290

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0086    |
| Data Size    | 444 bytes |
| Instructions | 50        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                   1E F0  FF FF 7F 6F 70 05 05 00        .....op...
0090: 5B 00 80 F1 30 0F 01 F1  30 0F 01 74 6C 6B 30 1D  [...0...0..tlk0.
00A0: 01 80 23 1D 07 80 23 5B  00 80 F1 30 0F 01 F1 30  ..#...#[...0...0
00B0: 0F 01 74 6C 6B 31 03 04  00 04 10 02 05 00 08 80  ..tlk1..........
00C0: 01 40 02 03 01 00 02 10  03 02 00 03 10 03 00 00  .@..............
00D0: 06 10 03 03 00 07 10 3E  04 00 08 80 E6 00 03 04  .......>........
00E0: 10 09 80 01 EB 00 03 04  10 08 80 3E 04 00 09 80  ...........>....
00F0: FA 00 03 05 10 09 80 01  FF 00 03 05 10 08 80 D4  ................
0100: 03 08 80 01 00 D4 03 09  80 02 00 D4 02 0A 80 06  ................
0110: 00 08 80 25 02 00 10 08  80 00 8A 01 02 04 10 08  ...%............
0120: 80 00 87 01 42 03 08 10  01 00 24 0B 80 08 80 08  ....B.....$.....
0130: 80 25 02 00 10 08 80 00  81 01 02 00 00 03 00 04  .%..............
0140: 64 01 5B 00 80 F1 30 0F  01 F1 30 0F 01 74 6C 6B  d.[...0...0..tlk
0150: 30 1D 0C 80 23 5B 00 80  F1 30 0F 01 F1 30 0F 01  0...#[...0...0..
0160: 74 6C 6B 31 03 01 10 09  80 43 00 43 01 03 04 00  tlk1.....C.C....
0170: 04 10 02 09 10 09 80 00  7E 01 1D 0D 80 23 01 81  ........~....#..
0180: 01 03 06 00 08 80 2E 01  3D 02 02 00 10 09 80 00  ........=.......
0190: 00 02 02 05 10 08 80 00  FD 01 42 03 08 10 02 00  ..........B.....
01A0: 24 0B 80 08 80 08 80 25  02 00 10 08 80 00 F7 01  $......%........
01B0: 02 00 00 03 00 04 DA 01  5B 00 80 F1 30 0F 01 F1  ........[...0...
01C0: 30 0F 01 74 6C 6B 30 1D  0C 80 23 5B 00 80 F1 30  0..tlk0...#[...0
01D0: 0F 01 F1 30 0F 01 74 6C  6B 31 03 01 10 0E 80 43  ...0..tlk1.....C
01E0: 00 43 01 03 04 00 04 10  02 09 10 09 80 00 F4 01  .C..............
01F0: 1D 0D 80 23 01 F7 01 03  06 00 08 80 2E 01 3D 02  ...#..........=.
0200: 02 00 10 0E 80 00 3A 02  5B 00 80 F1 30 0F 01 F1  ......:.[...0...
0210: 30 0F 01 74 6C 6B 30 1D  02 80 23 1D 03 80 23 1D  0..tlk0...#...#.
0220: 04 80 23 5B 00 80 F1 30  0F 01 F1 30 0F 01 74 6C  ..#[...0...0..tl
0230: 6B 31 03 06 00 0E 80 01  3D 02 06 05 00 01 BB 00  k1......=.......
0240: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0086 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x008B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x008C [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x008D [0x05] ExtData[1]->WorkLocal[5] = 1
  4: 0x0090 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Chacharoon (ID: 17772785/0x010F30F1), Chacharoon (ID: 17772785/0x010F30F1)], work=3566*
  5: 0x009F [0x1D] PRINT_EVENT_MESSAGE(message_id=16013*)
    → "Happy Happy New Year!"
  6: 0x00A2 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x00A3 [0x1D] PRINT_EVENT_MESSAGE(message_id=16014*)
    → "Chacharoon wishing you very best in New Year the Qiqirn way--by giving you things for $5 jingly!"
  8: 0x00A6 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x00A7 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [Chacharoon (ID: 17772785/0x010F30F1), Chacharoon (ID: 17772785/0x010F30F1)], work=3566*
 10: 0x00B6 [0x03] ExtData[1]->WorkLocal[4] = Work_Zone[4]
 11: 0x00BB [0x02] IF !(ExtData[1]->WorkLocal[5] == 0*) GOTO 0x0240
 12: 0x00C3 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[2]
 13: 0x00C8 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[3]
 14: 0x00CD [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[6]
 15: 0x00D2 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[7]
 16: 0x00D7 [0x3E] IF !(ExtData[1]->WorkLocal[4] bit 0*) GOTO 0x00E6
 17: 0x00DE [0x03] Work_Zone[4] = 1*
 18: 0x00E3 [0x01] GOTO 0x00EB
 19: 0x00E6 [0x03] Work_Zone[4] = 0*

SUBROUTINE_00EB:
 20: 0x00EB [0x3E] IF !(ExtData[1]->WorkLocal[4] bit 1*) GOTO 0x00FA
 21: 0x00F2 [0x03] Work_Zone[5] = 1*
 22: 0x00F7 [0x01] GOTO 0x00FF
 23: 0x00FA [0x03] Work_Zone[5] = 0*

SUBROUTINE_00FF:
 24: 0x00FF [0xD4] MAP_QUERY_WINDOW: Prepare buffer configuration A (buffer=[08 80 01 00 D4 03 09 80...])
 25: 0x011D [0x04] DEPRECATED_NOP(unused=0x0810)
 26: 0x0120 [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 1107396352/0x42018700))
 27: 0x0125 [0x03] Work_Zone[8] = ExtData[1]->WorkLocal[1]
 28: 0x012A [0x24] CREATE_DIALOG(message_id=16016*, default_option=0*, option_flags=0*)
    → "@Buy $6 for $5 gil? [Yes./No.]"
 29: 0x0131 [0x25] WAIT_DIALOG_SELECT()
 30: 0x0132 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0181
 31: 0x013A [0x02] IF !(ExtData[1]->WorkLocal[0] < ExtData[1]->WorkLocal[3]) GOTO 0x0164
 32: 0x0142 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Chacharoon (ID: 17772785/0x010F30F1), Chacharoon (ID: 17772785/0x010F30F1)], work=3566*
 33: 0x0151 [0x1D] PRINT_EVENT_MESSAGE(message_id=16017*)
    → "Ooooh, $6! What is inside? Maybe you get something special!"
 34: 0x0154 [0x23] WAIT_FOR_DIALOG_INTERACTION
 35: 0x0155 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [Chacharoon (ID: 17772785/0x010F30F1), Chacharoon (ID: 17772785/0x010F30F1)], work=3566*
 36: 0x0164 [0x03] Work_Zone[1] = 1*
 37: 0x0169 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 38: 0x016B [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 39: 0x016D [0x03] ExtData[1]->WorkLocal[4] = Work_Zone[4]
 40: 0x0172 [0x02] IF !(Work_Zone[9] == 1*) GOTO 0x017E
 41: 0x017A [0x1D] PRINT_EVENT_MESSAGE(message_id=16018*)
    → "Not enough jingly? Then you go out, get more jingly, and bring back. Deal?"
 42: 0x017D [0x23] WAIT_FOR_DIALOG_INTERACTION
 43: 0x017E [0x01] GOTO 0x0181

SUBROUTINE_0181:
 44: 0x0181 [0x03] ExtData[1]->WorkLocal[6] = 0*
 45: 0x0186 [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
 46: 0x0187 [0x01] GOTO 0x023D

SUBROUTINE_023D:
 47: 0x023D [0x01] GOTO 0x00BB
 48: 0x0240 [0x21] END_EVENT
 49: 0x0241 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x018A [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0200
     0x0192 [0x02] IF !(Work_Zone[5] == 0*) GOTO 0x01FD
     0x019A [0x42] SET_CLI_EVENT_CANCEL_DATA()
     0x019B [0x03] Work_Zone[8] = ExtData[1]->WorkLocal[2]
     0x01A0 [0x24] CREATE_DIALOG(message_id=16016*, default_option=0*, option_flags=0*)
    → "@Buy $6 for $5 gil? [Yes./No.]"
     0x01A7 [0x25] WAIT_DIALOG_SELECT()
     0x01A8 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01F7
     0x01B0 [0x02] IF !(ExtData[1]->WorkLocal[0] < ExtData[1]->WorkLocal[3]) GOTO 0x01DA
     0x01B8 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Chacharoon (ID: 17772785/0x010F30F1), Chacharoon (ID: 17772785/0x010F30F1)], work=3566*
     0x01C7 [0x1D] PRINT_EVENT_MESSAGE(message_id=16017*)
    → "Ooooh, $6! What is inside? Maybe you get something special!"
     0x01CA [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x01CB [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [Chacharoon (ID: 17772785/0x010F30F1), Chacharoon (ID: 17772785/0x010F30F1)], work=3566*
     0x01DA [0x03] Work_Zone[1] = 2*
     0x01DF [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
     0x01E1 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
     0x01E3 [0x03] ExtData[1]->WorkLocal[4] = Work_Zone[4]
     0x01E8 [0x02] IF !(Work_Zone[9] == 1*) GOTO 0x01F4
     0x01F0 [0x1D] PRINT_EVENT_MESSAGE(message_id=16018*)
    → "Not enough jingly? Then you go out, get more jingly, and bring back. Deal?"
     0x01F3 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x01F4 [0x01] GOTO 0x01F7
     0x01F7 [0x03] ExtData[1]->WorkLocal[6] = 0*
     0x01FC [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
     0x01FD [0x01] GOTO 0x023D
     0x0200 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x023A
     0x0208 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Chacharoon (ID: 17772785/0x010F30F1), Chacharoon (ID: 17772785/0x010F30F1)], work=3566*
     0x0217 [0x1D] PRINT_EVENT_MESSAGE(message_id=16019*)
    → "In homeland, people put jingly in pouches and give to other people they like!"
     0x021A [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x021B [0x1D] PRINT_EVENT_MESSAGE(message_id=16020*)
    → "You give me jingly, I put in pouch. Then I give you pouch for you to give to friends. Okay?"
     0x021E [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x021F [0x1D] PRINT_EVENT_MESSAGE(message_id=16021*)
    → "But you cannot open pouch yourself. Only friend can. Must be Mysterious Moogle Magic."
     0x0222 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x0223 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [Chacharoon (ID: 17772785/0x010F30F1), Chacharoon (ID: 17772785/0x010F30F1)], work=3566*
     0x0232 [0x03] ExtData[1]->WorkLocal[6] = 2*
     0x0237 [0x01] GOTO 0x023D
     0x023A [0x06] ExtData[1]->WorkLocal[5] = 0
```
