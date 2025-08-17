# 17743891 - Bartolomeo

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Port Bastok (ID: 236) |
| Block Size       | 384 bytes             |
| Total Events     | 3                     |
| References Count | 14                    |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [140](#event-140)     | 0x0001       |      1 |              1 |
| [52](#event-52)       | 0x0002       |    296 |             47 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x013C      |         316 |
|       1 | 0x00C8      |         200 |
|       2 | 0x0000      |           0 |
|       3 | 0x001E      |          30 |
|       4 | 0x0003      |           3 |
|       5 | 0x0088      |         136 |
|       6 | 0x1CC5      |        7365 |
|       7 | 0x0078      |         120 |
|       8 | 0x003C      |          60 |
|       9 | 0x307F      |       12415 |
|      10 | 0x1CC6      |        7366 |
|      11 | 0x1CC7      |        7367 |
|      12 | 0x1CC8      |        7368 |
|      13 | 0x1CC9      |        7369 |

## String References

- **7365**: May I help you? ...A white mage named Evrain? No, I'm sorry, I don't think I've seen him.

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

### Event 140

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 52

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0002    |
| Data Size    | 296 bytes |
| Instructions | 47        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       42 75 00 00 80 75  01 1E F0 FF FF 7F 45 01    Bu...u......E.
0010: 80 F8 FF FF 7F F8 FF FF  7F 66 64 6F 30 02 80 1C  .........fdo0...
0020: 03 80 38 04 80 29 0A F0  FF FF 7F 0D 1E F0 FF FF  ..8..)..........
0030: 7F 46 01 45 05 80 F8 FF  FF 7F F8 FF FF 7F 73 30  .F.E..........s0
0040: 34 30 02 80 45 01 80 F8  FF FF 7F F8 FF FF 7F 66  40..E..........f
0050: 64 69 30 02 80 1C 03 80  27 64 56 C0 0E 01 03 27  di0.....'dV....'
0060: 64 16 C0 0E 01 02 1D 06  80 23 1C 03 80 45 05 80  d........#...E..
0070: F8 FF FF 7F F8 FF FF 7F  73 30 34 31 02 80 1C 07  ........s041....
0080: 80 4A F0 FF FF 7F 16 C0  0E 01 1C 03 80 1E 16 C0  .J..............
0090: 0E 01 1C 08 80 03 09 10  09 80 2B 16 C0 0E 01 0A  ..........+.....
00A0: 80 23 2A 64 16 C0 0E 01  66 02 80 16 C0 0E 01 16  .#*d....f.......
00B0: C0 0E 01 74 6C 6B 30 2B  16 C0 0E 01 0B 80 23 2B  ...tlk0+......#+
00C0: 16 C0 0E 01 0C 80 23 66  02 80 16 C0 0E 01 16 C0  ......#f........
00D0: 0E 01 74 65 6E 30 2B 16  C0 0E 01 0D 80 23 53 16  ..ten0+......#S.
00E0: C0 0E 01 16 C0 0E 01 74  65 6E 30 27 64 16 C0 0E  .......ten0'd...
00F0: 01 03 1C 08 80 4A F0 FF  FF 7F 16 C0 0E 01 45 01  .....J........E.
0100: 80 F8 FF FF 7F F8 FF FF  7F 66 64 6F 31 02 80 1C  .........fdo1...
0110: 08 80 46 00 1C 03 80 45  01 80 F8 FF FF 7F F8 FF  ..F....E........
0120: FF 7F 66 64 69 30 02 80  21 00                    ..fdi0..!.      
```

#### Opcodes

```
  0: 0x0002 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0003 [0x75] LOAD_ROOM(Load indoor room, room=316*)
  2: 0x0007 [0x75] LOAD_ROOM(No action)
  3: 0x0009 [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x000E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [EventEntity, EventEntity], work=[200*, 0*]
  5: 0x001F [0x1C] WAIT(30* ticks)
  6: 0x0022 [0x38] SET_CLIENT_EVENT_MODE(mode=3*)
  7: 0x0025 [0x29] REQ_SET_WAIT(priority=0x0A, entity_id=LocalPlayer, tag_num=0x0D)
  8: 0x002C [0x1E] EventEntity looks at LocalPlayer and starts talking
  9: 0x0031 [0x46] CAMERA_CONTROL: Disable user control
 10: 0x0033 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s040" with entities [EventEntity, EventEntity], work=[136*, 0*]
 11: 0x0044 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi0" with entities [EventEntity, EventEntity], work=[200*, 0*]
 12: 0x0055 [0x1C] WAIT(30* ticks)
 13: 0x0058 [0x27] REQ_SET(priority=0x64, entity_id=Door:Arrivals Entrance (ID: 17743958/0x010EC056), tag_num=0x03)
 14: 0x005F [0x27] REQ_SET(priority=0x64, entity_id=Evrain (ID: 17743894/0x010EC016), tag_num=0x02)
 15: 0x0066 [0x1D] PRINT_EVENT_MESSAGE(message_id=7365*)
    → "May I help you? ...A white mage named Evrain? No, I'm sorry, I don't think I've seen him."
 16: 0x0069 [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x006A [0x1C] WAIT(30* ticks)
 18: 0x006D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s041" with entities [EventEntity, EventEntity], work=[136*, 0*]
 19: 0x007E [0x1C] WAIT(120* ticks)
 20: 0x0081 [0x4A] LocalPlayer looks at Evrain (ID: 17743894/0x010EC016)
 21: 0x008A [0x1C] WAIT(30* ticks)
 22: 0x008D [0x1E] EventEntity looks at Evrain (ID: 17743894/0x010EC016) and starts talking
 23: 0x0092 [0x1C] WAIT(60* ticks)
 24: 0x0095 [0x03] Work_Zone[9] = 12415*
 25: 0x009A [0x2B] Evrain (ID: 17743894/0x010EC016) [7366*]:
    → "That $7... You must be Mister Powhatan."
 26: 0x00A1 [0x23] WAIT_FOR_DIALOG_INTERACTION
 27: 0x00A2 [0x2A] GET_REQ_LEVEL(level=100, entity_id=Evrain (ID: 17743894/0x010EC016))
 28: 0x00A8 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Evrain (ID: 17743894/0x010EC016), Evrain (ID: 17743894/0x010EC016)], work=0*
 29: 0x00B7 [0x2B] Evrain (ID: 17743894/0x010EC016) [7367*]:
    → "No? You've come in his place? Mister Powhatan is in the tavern, you say?"
 30: 0x00BE [0x23] WAIT_FOR_DIALOG_INTERACTION
 31: 0x00BF [0x2B] Evrain (ID: 17743894/0x010EC016) [7368*]:
    → "He shouldn't have gone through all this trouble for me, you know. I've been to Bastok before."
 32: 0x00C6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 33: 0x00C7 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "ten0" with entities [Evrain (ID: 17743894/0x010EC016), Evrain (ID: 17743894/0x010EC016)], work=0*
 34: 0x00D6 [0x2B] Evrain (ID: 17743894/0x010EC016) [7369*]:
    → "I'll go meet him in the tavern, then. Don't worry, I know the way."
 35: 0x00DD [0x23] WAIT_FOR_DIALOG_INTERACTION
 36: 0x00DE [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ten0" with entities [Evrain (ID: 17743894/0x010EC016), Evrain (ID: 17743894/0x010EC016)]
 37: 0x00EB [0x27] REQ_SET(priority=0x64, entity_id=Evrain (ID: 17743894/0x010EC016), tag_num=0x03)
 38: 0x00F2 [0x1C] WAIT(60* ticks)
 39: 0x00F5 [0x4A] LocalPlayer looks at Evrain (ID: 17743894/0x010EC016)
 40: 0x00FE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 41: 0x010F [0x1C] WAIT(60* ticks)
 42: 0x0112 [0x46] CAMERA_CONTROL: Restore default settings
 43: 0x0114 [0x1C] WAIT(30* ticks)
 44: 0x0117 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi0" with entities [EventEntity, EventEntity], work=[200*, 0*]
 45: 0x0128 [0x21] END_EVENT
 46: 0x0129 [0x00] END_REQSTACK()
```
