# 16990631 - Kamih Mapokhalam

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Bhaflau Thickets (ID: 52) |
| Block Size       | 744 bytes                 |
| Total Events     | 10                        |
| References Count | 34                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [120](#event-120)     | 0x0001       |     51 |             20 |
| [121](#event-121)     | 0x0034       |    158 |             30 |
| [122](#event-122)     | 0x00D2       |    237 |             45 |
| [128](#event-128)     | 0x01BF       |     14 |              4 |
| [129](#event-129)     | 0x01CD       |      4 |              2 |
| [130](#event-130)     | 0x01D1       |     14 |              4 |
| [131](#event-131)     | 0x01DF       |      4 |              2 |
| [146](#event-146)     | 0x01E3       |     39 |             14 |
| [147](#event-147)     | 0x020A       |     27 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1CB2      |        7346 |
|       1 | 0x1CB3      |        7347 |
|       2 | 0x1CB4      |        7348 |
|       3 | 0x0889      |        2185 |
|       4 | 0x0001      |           1 |
|       5 | 0x1CB5      |        7349 |
|       6 | 0x088A      |        2186 |
|       7 | 0x0003      |           3 |
|       8 | 0x1CBA      |        7354 |
|       9 | 0x0004      |           4 |
|      10 | 0x00C8      |         200 |
|      11 | 0x0000      |           0 |
|      12 | 0x003C      |          60 |
|      13 | 0x0013      |          19 |
|      14 | 0x00D9      |         217 |
|      15 | 0x1CB6      |        7350 |
|      16 | 0x0078      |         120 |
|      17 | 0x1CB7      |        7351 |
|      18 | 0x1CB8      |        7352 |
|      19 | 0x00B4      |         180 |
|      20 | 0x00F0      |         240 |
|      21 | 0x000D      |          13 |
|      22 | 0x54D2      |       21714 |
|      23 | 0x91FD7     |      597975 |
|      24 | 0xFFFF92A0  |  4294939296 |
|      25 | 0x0800      |        2048 |
|      26 | 0x4E2F      |       20015 |
|      27 | 0x91FDD     |      597981 |
|      28 | 0xFFFF87F7  |  4294936567 |
|      29 | 0x0400      |        1024 |
|      30 | 0x0749      |        1865 |
|      31 | 0x1CBB      |        7355 |
|      32 | 0x0020      |          32 |
|      33 | 0x1CBC      |        7356 |

## String References

- **7346**: This tunnel leads to the Alzadaal Undersea Ruins.
- **7347**: Now that the investigation of the Aht Urhgan Archaelogical Research Institute has drawn to a close, the ruins have been opened to the public.
- **7348**: However we cannot guarantee your safety--you would be wise to stay aware of your surroundings.
- **7349**: The fee for entering the ruins comes to $1 $0 .
- **7350**: Very well. You may proceed.
- **7351**: Heading outside? Please be aware that you will be required to pay a fee if you wish to reenter the ruins.
- **7352**: Leave the ruins? [Yes, I'm done here./Not just yet.]
- **7354**: If you need a map of the ruins, you can purchase one for $1 $0 .
- **7355**: Here is your $3. Keep it in a safe place.
- **7356**: You already possess a map of the ruins. I only have a limited number of copies, so please use the one you have.

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

### Event 120

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 51 bytes |
| Instructions | 20       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 1E F0 FF FF 7F  6F 70 1D 00 80 23 1D 01    ......op...#..
0010: 80 23 1D 02 80 23 03 02  10 03 80 03 03 10 04 80  .#...#..........
0020: 1D 05 80 23 03 02 10 06  80 03 03 10 07 80 1D 08  ...#............
0030: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0008 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0009 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x000A [0x1D] PRINT_EVENT_MESSAGE(message_id=7346*)
    → "This tunnel leads to the Alzadaal Undersea Ruins."
  5: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x000E [0x1D] PRINT_EVENT_MESSAGE(message_id=7347*)
    → "Now that the investigation of the Aht Urhgan Archaelogical Research Institute has drawn to a close, the ruins have been opened to the public."
  7: 0x0011 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0012 [0x1D] PRINT_EVENT_MESSAGE(message_id=7348*)
    → "However we cannot guarantee your safety--you would be wise to stay aware of your surroundings."
  9: 0x0015 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0016 [0x03] Work_Zone[2] = 2185*
 11: 0x001B [0x03] Work_Zone[3] = 1*
 12: 0x0020 [0x1D] PRINT_EVENT_MESSAGE(message_id=7349*)
    → "The fee for entering the ruins comes to $1 $0 ."
 13: 0x0023 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x0024 [0x03] Work_Zone[2] = 2186*
 15: 0x0029 [0x03] Work_Zone[3] = 3*
 16: 0x002E [0x1D] PRINT_EVENT_MESSAGE(message_id=7354*)
    → "If you need a map of the ruins, you can purchase one for $1 $0 ."
 17: 0x0031 [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x0032 [0x21] END_EVENT
 19: 0x0033 [0x00] END_REQSTACK()
```

### Event 121

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0034    |
| Data Size    | 158 bytes |
| Instructions | 30        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:             20 01 42 43  00 43 01 46 01 42 38 09       .BC.C.F.B8.
0040: 80 45 0A 80 F0 FF FF 7F  F0 FF FF 7F 66 64 6F 31  .E..........fdo1
0050: 0B 80 1C 0C 80 38 0D 80  45 0E 80 F0 FF FF 7F F0  .....8..E.......
0060: FF FF 7F 61 6C 6B 31 0B  80 29 01 F0 FF FF 7F 0D  ...alk1..)......
0070: 45 0A 80 F0 FF FF 7F F0  FF FF 7F 66 64 69 31 0B  E..........fdi1.
0080: 80 1C 0C 80 1D 0F 80 1C  0C 80 29 01 A7 41 03 01  ..........)..A..
0090: 04 29 01 A7 41 03 01 05  29 01 A5 41 03 01 01 1C  .)..A...)..A....
00A0: 0C 80 27 01 F0 FF FF 7F  0E 1C 10 80 45 0A 80 F0  ..'.........E...
00B0: FF FF 7F F0 FF FF 7F 66  64 6F 31 0B 80 1C 0C 80  .......fdo1.....
00C0: 03 01 10 04 80 29 01 A5  41 03 01 02 46 00 20 00  .....)..A...F. .
00D0: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0034 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0036 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0037 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  3: 0x0039 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  4: 0x003B [0x46] CAMERA_CONTROL: Disable user control
  5: 0x003D [0x42] SET_CLI_EVENT_CANCEL_DATA()
  6: 0x003E [0x38] SET_CLIENT_EVENT_MODE(mode=4*)
  7: 0x0041 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  8: 0x0052 [0x1C] WAIT(60* ticks)
  9: 0x0055 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 10: 0x0058 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "alk1" with entities [LocalPlayer, LocalPlayer], work=[217*, 0*]
 11: 0x0069 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x0D)
 12: 0x0070 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 13: 0x0081 [0x1C] WAIT(60* ticks)
 14: 0x0084 [0x1D] PRINT_EVENT_MESSAGE(message_id=7350*)
    → "Very well. You may proceed."
 15: 0x0087 [0x1C] WAIT(60* ticks)
 16: 0x008A [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Kamih Mapokhalam (ID: 16990631/0x010341A7), tag_num=0x04)
 17: 0x0091 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Kamih Mapokhalam (ID: 16990631/0x010341A7), tag_num=0x05)
 18: 0x0098 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Door_1g3 (ID: 16990629/0x010341A5), tag_num=0x01)
 19: 0x009F [0x1C] WAIT(60* ticks)
 20: 0x00A2 [0x27] REQ_SET(priority=0x01, entity_id=LocalPlayer, tag_num=0x0E)
 21: 0x00A9 [0x1C] WAIT(120* ticks)
 22: 0x00AC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 23: 0x00BD [0x1C] WAIT(60* ticks)
 24: 0x00C0 [0x03] Work_Zone[1] = 1*
 25: 0x00C5 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Door_1g3 (ID: 16990629/0x010341A5), tag_num=0x02)
 26: 0x00CC [0x46] CAMERA_CONTROL: Restore default settings
 27: 0x00CE [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 28: 0x00D0 [0x21] END_EVENT
 29: 0x00D1 [0x00] END_REQSTACK()
```

### Event 122

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00D2    |
| Data Size    | 237 bytes |
| Instructions | 45        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:       20 01 42 1E F0 FF  FF 7F 6F 70 1D 11 80 23     .B.....op...#
00E0: 24 12 80 04 80 0B 80 25  02 00 10 0B 80 00 AB 01  $......%........
00F0: 43 00 43 01 46 01 42 45  0A 80 F0 FF FF 7F F0 FF  C.C.F.BE........
0100: FF 7F 66 64 6F 31 0B 80  1C 0C 80 38 0D 80 45 0E  ..fdo1.....8..E.
0110: 80 F0 FF FF 7F F0 FF FF  7F 61 6C 6B 31 0B 80 29  .........alk1..)
0120: 01 F0 FF FF 7F 11 29 01  F0 FF FF 7F 0F 45 0A 80  ......)......E..
0130: F0 FF FF 7F F0 FF FF 7F  66 64 69 31 0B 80 1C 0C  ........fdi1....
0140: 80 29 01 A7 41 03 01 04  29 01 A7 41 03 01 05 29  .)..A...)..A...)
0150: 01 A5 41 03 01 01 1C 0C  80 27 01 F0 FF FF 7F 10  ..A......'......
0160: 1C 13 80 29 01 A7 41 03  01 06 29 01 A7 41 03 01  ...)..A...)..A..
0170: 07 45 0A 80 F0 FF FF 7F  F0 FF FF 7F 66 64 6F 31  .E..........fdo1
0180: 0B 80 1C 0C 80 03 01 10  04 80 29 01 A5 41 03 01  ..........)..A..
0190: 02 46 00 2E 1C 14 80 45  0A 80 F0 FF FF 7F F0 FF  .F.....E........
01A0: FF 7F 66 64 69 31 0B 80  01 BB 01 02 00 10 04 80  ..fdi1..........
01B0: 00 BB 01 03 01 10 0B 80  01 BB 01 20 00 21 00     ........... .!. 
```

#### Opcodes

```
  0: 0x00D2 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x00D4 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x00D5 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x00DA [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00DB [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  5: 0x00DC [0x1D] PRINT_EVENT_MESSAGE(message_id=7351*)
    → "Heading outside? Please be aware that you will be required to pay a fee if you wish to reenter the ruins."
  6: 0x00DF [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x00E0 [0x24] CREATE_DIALOG(message_id=7352*, default_option=1*, option_flags=0*)
    → "Leave the ruins? [Yes, I'm done here./Not just yet.]"
  8: 0x00E7 [0x25] WAIT_DIALOG_SELECT()
  9: 0x00E8 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01AB
 10: 0x00F0 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 11: 0x00F2 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 12: 0x00F4 [0x46] CAMERA_CONTROL: Disable user control
 13: 0x00F6 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 14: 0x00F7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 15: 0x0108 [0x1C] WAIT(60* ticks)
 16: 0x010B [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 17: 0x010E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "alk1" with entities [LocalPlayer, LocalPlayer], work=[217*, 0*]
 18: 0x011F [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x11)
 19: 0x0126 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x0F)
 20: 0x012D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 21: 0x013E [0x1C] WAIT(60* ticks)
 22: 0x0141 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Kamih Mapokhalam (ID: 16990631/0x010341A7), tag_num=0x04)
 23: 0x0148 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Kamih Mapokhalam (ID: 16990631/0x010341A7), tag_num=0x05)
 24: 0x014F [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Door_1g3 (ID: 16990629/0x010341A5), tag_num=0x01)
 25: 0x0156 [0x1C] WAIT(60* ticks)
 26: 0x0159 [0x27] REQ_SET(priority=0x01, entity_id=LocalPlayer, tag_num=0x10)
 27: 0x0160 [0x1C] WAIT(180* ticks)
 28: 0x0163 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Kamih Mapokhalam (ID: 16990631/0x010341A7), tag_num=0x06)
 29: 0x016A [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Kamih Mapokhalam (ID: 16990631/0x010341A7), tag_num=0x07)
 30: 0x0171 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 31: 0x0182 [0x1C] WAIT(60* ticks)
 32: 0x0185 [0x03] Work_Zone[1] = 1*
 33: 0x018A [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Door_1g3 (ID: 16990629/0x010341A5), tag_num=0x02)
 34: 0x0191 [0x46] CAMERA_CONTROL: Restore default settings
 35: 0x0193 [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
 36: 0x0194 [0x1C] WAIT(240* ticks)
 37: 0x0197 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 38: 0x01A8 [0x01] GOTO 0x01BB
 39: 0x01AB [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x01BB
 40: 0x01B3 [0x03] Work_Zone[1] = 0*
 41: 0x01B8 [0x01] GOTO 0x01BB

SUBROUTINE_01BB:
 42: 0x01BB [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 43: 0x01BD [0x21] END_EVENT
 44: 0x01BE [0x00] END_REQSTACK()
```

### Event 128

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01BF   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:                                               32                 2
01C0: 15 80 1F 00 16 80 17 80  18 80 1F 01 00           .............   
```

#### Opcodes

```
  0: 0x01BF [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x01C2 [0x1F] MOVE_ENTITY: EventEntity moves to X=21.714*, Z=597.975*, Y=-28.000*
  2: 0x01CA [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x01CC [0x00] END_REQSTACK()
```

### Event 129

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01CD  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0:                                         39 19 80               9..
01D0: 00                                                .               
```

#### Opcodes

```
  0: 0x01CD [0x39] SET_ENTITY_DIRECTION(direction=11.2°*)
  1: 0x01D0 [0x00] END_REQSTACK()
```

### Event 130

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01D1   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01D0:    32 15 80 1F 00 1A 80  1B 80 1C 80 1F 01 00      2............. 
```

#### Opcodes

```
  0: 0x01D1 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x01D4 [0x1F] MOVE_ENTITY: EventEntity moves to X=20.015*, Z=597.981*, Y=-30.729*
  2: 0x01DC [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x01DE [0x00] END_REQSTACK()
```

### Event 131

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01DF  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01D0:                                               39                 9
01E0: 1D 80 00                                          ...             
```

#### Opcodes

```
  0: 0x01DF [0x39] SET_ENTITY_DIRECTION(direction=5.6°*)
  1: 0x01E2 [0x00] END_REQSTACK()
```

### Event 146

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01E3   |
| Data Size    | 39 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01E0:          20 01 42 43 00  43 01 1E F0 FF FF 7F 6F      .BC.C......o
01F0: 70 6E A7 41 03 01 0B 80  99 A7 41 03 01 03 02 10  pn.A......A.....
0200: 1E 80 1D 1F 80 1C 13 80  21 00                    ........!.      
```

#### Opcodes

```
  0: 0x01E3 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x01E5 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x01E6 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  3: 0x01E8 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  4: 0x01EA [0x1E] EventEntity looks at LocalPlayer and starts talking
  5: 0x01EF [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x01F0 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  7: 0x01F1 [0x6E] Kamih Mapokhalam (ID: 16990631/0x010341A7) uses emote 0*
  8: 0x01F8 [0x99] Wait for Kamih Mapokhalam (ID: 16990631/0x010341A7) animation to complete
  9: 0x01FD [0x03] Work_Zone[2] = 1865*
 10: 0x0202 [0x1D] PRINT_EVENT_MESSAGE(message_id=7355*)
    → "Here is your $3. Keep it in a safe place."
 11: 0x0205 [0x1C] WAIT(180* ticks)
 12: 0x0208 [0x21] END_EVENT
 13: 0x0209 [0x00] END_REQSTACK()
```

### Event 147

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x020A   |
| Data Size    | 27 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0200:                                20 01 1E F0 FF FF             .....
0210: 7F 6F 70 6E A7 41 03 01  20 80 99 A7 41 03 01 1D  .opn.A.. ...A...
0220: 21 80 23 21 00                                    !.#!.           
```

#### Opcodes

```
  0: 0x020A [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x020C [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0211 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0212 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0213 [0x6E] Kamih Mapokhalam (ID: 16990631/0x010341A7) uses emote 32*
  5: 0x021A [0x99] Wait for Kamih Mapokhalam (ID: 16990631/0x010341A7) animation to complete
  6: 0x021F [0x1D] PRINT_EVENT_MESSAGE(message_id=7356*)
    → "You already possess a map of the ruins. I only have a limited number of copies, so please use the one you have."
  7: 0x0222 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0223 [0x21] END_EVENT
  9: 0x0224 [0x00] END_REQSTACK()
```
