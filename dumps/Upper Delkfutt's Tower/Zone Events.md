# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Upper Delkfutt's Tower (ID: 158) |
| Block Size       | 1024 bytes                       |
| Total Events     | 16                               |
| References Count | 55                               |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [65534](#event-65534) | 0x0001       |      1 |              1 |
| [0](#event-0)         | 0x0002       |     84 |             17 |
| [1](#event-1)         | 0x0056       |     84 |             17 |
| [3](#event-3)         | 0x00AA       |     23 |              5 |
| [4](#event-4)         | 0x00C1       |     21 |              5 |
| [13](#event-13)       | 0x00D6       |     23 |              5 |
| [5](#event-5)         | 0x00ED       |     94 |             13 |
| [7](#event-7)         | 0x014B       |     57 |             10 |
| [8](#event-8)         | 0x0184       |     57 |             10 |
| [9](#event-9)         | 0x01BD       |     57 |             10 |
| [10](#event-10)       | 0x01F6       |     57 |             10 |
| [11](#event-11)       | 0x022F       |     13 |              3 |
| [12](#event-12)       | 0x023C       |     14 |              4 |
| [14](#event-14)       | 0x024A       |     50 |              8 |
| [18](#event-18)       | 0x027C       |     88 |             22 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0018      |          24 |
|       1 | 0x0001      |           1 |
|       2 | 0x0000      |           0 |
|       3 | 0x008C      |         140 |
|       4 | 0x00C8      |         200 |
|       5 | 0x003C      |          60 |
|       6 | 0xFFFB7FA6  |  4294672294 |
|       7 | 0x3AEB      |       15083 |
|       8 | 0xFFFDCEFB  |  4294823675 |
|       9 | 0x09F7      |        2551 |
|      10 | 0xFFFB6D4F  |  4294667599 |
|      11 | 0x4C29      |       19497 |
|      12 | 0x09F5      |        2549 |
|      13 | 0x000D      |          13 |
|      14 | 0xFFFB6D13  |  4294667539 |
|      15 | 0x4DA2      |       19874 |
|      16 | 0xFFFE3A6F  |  4294851183 |
|      17 | 0xFFFB503A  |  4294660154 |
|      18 | 0x530A      |       21258 |
|      19 | 0xFFFE3AAD  |  4294851245 |
|      20 | 0x08D4      |        2260 |
|      21 | 0xFFFB400B  |  4294656011 |
|      22 | 0x58C0      |       22720 |
|      23 | 0xFFFE3A5D  |  4294851165 |
|      24 | 0xFFFB3F74  |  4294655860 |
|      25 | 0x5966      |       22886 |
|      26 | 0xFFFE3A55  |  4294851157 |
|      27 | 0x0544      |        1348 |
|      28 | 0x0002      |           2 |
|      29 | 0x00AA      |         170 |
|      30 | 0x2504      |        9476 |
|      31 | 0x610C      |       24844 |
|      32 | 0xFFFE7578  |  4294866296 |
|      33 | 0x03EE      |        1006 |
|      34 | 0xFFFB9152  |  4294676818 |
|      35 | 0x6194      |       24980 |
|      36 | 0xFFFE5F03  |  4294860547 |
|      37 | 0x0374      |         884 |
|      38 | 0x3CE0D     |      249357 |
|      39 | 0x6150      |       24912 |
|      40 | 0xFFFF6F78  |  4294930296 |
|      41 | 0x03FB      |        1019 |
|      42 | 0x767D      |       30333 |
|      43 | 0x621E      |       25118 |
|      44 | 0xFFFF5903  |  4294924547 |
|      45 | 0x03DC      |         988 |
|      46 | 0x4D8E0     |      317664 |
|      47 | 0x4E72      |       20082 |
|      48 | 0x3E80      |       16000 |
|      49 | 0x0FED      |        4077 |
|      50 | 0x508B0     |      329904 |
|      51 | 0x4E39      |       20025 |
|      52 | 0x0064      |         100 |
|      53 | 0x1CD7      |        7383 |
|      54 | 0x1CD4      |        7380 |

## String References

- **24**: Use the device? [Yes./No.]
- **7380**: Touch the crystal? [Yes./No.]
- **7383**: Touch the crystal? [Yes./No.]

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

### Event 65534

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

### Event 0

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 84 bytes |
| Instructions | 17       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       20 01 24 00 80 01  80 02 80 25 02 00 10 02     .$......%....
0010: 80 00 49 00 42 43 00 43  01 03 01 10 01 80 62 01  ..I.BC.C......b.
0020: 80 F0 FF FF 7F F0 FF FF  7F 6D 61 69 6E 02 80 1C  .........main...
0030: 03 80 45 04 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F  ..E..........fdo
0040: 31 02 80 1C 05 80 01 54  00 02 00 10 01 80 00 54  1......T.......T
0050: 00 01 54 00 21 00                                 ..T.!.          
```

#### Opcodes

```
  0: 0x0002 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0004 [0x24] CREATE_DIALOG(message_id=24*, default_option=1*, option_flags=0*)
    → "Use the device? [Yes./No.]"
  2: 0x000B [0x25] WAIT_DIALOG_SELECT()
  3: 0x000C [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0049
  4: 0x0014 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x0015 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  6: 0x0017 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  7: 0x0019 [0x03] Work_Zone[1] = 1*
  8: 0x001E [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
  9: 0x002F [0x1C] WAIT(140* ticks)
 10: 0x0032 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 11: 0x0043 [0x1C] WAIT(60* ticks)
 12: 0x0046 [0x01] GOTO 0x0054
 13: 0x0049 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0054
 14: 0x0051 [0x01] GOTO 0x0054

SUBROUTINE_0054:
 15: 0x0054 [0x21] END_EVENT
 16: 0x0055 [0x00] END_REQSTACK()
```

### Event 1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0056   |
| Data Size    | 84 bytes |
| Instructions | 17       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                   20 01  24 00 80 01 80 02 80 25         .$......%
0060: 02 00 10 02 80 00 9D 00  42 43 00 43 01 03 01 10  ........BC.C....
0070: 01 80 62 01 80 F0 FF FF  7F F0 FF FF 7F 6D 61 69  ..b..........mai
0080: 6E 02 80 1C 03 80 45 04  80 F0 FF FF 7F F0 FF FF  n.....E.........
0090: 7F 66 64 6F 31 02 80 1C  05 80 01 A8 00 02 00 10  .fdo1...........
00A0: 01 80 00 A8 00 01 A8 00  21 00                    ........!.      
```

#### Opcodes

```
  0: 0x0056 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0058 [0x24] CREATE_DIALOG(message_id=24*, default_option=1*, option_flags=0*)
    → "Use the device? [Yes./No.]"
  2: 0x005F [0x25] WAIT_DIALOG_SELECT()
  3: 0x0060 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x009D
  4: 0x0068 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x0069 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  6: 0x006B [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  7: 0x006D [0x03] Work_Zone[1] = 1*
  8: 0x0072 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
  9: 0x0083 [0x1C] WAIT(140* ticks)
 10: 0x0086 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 11: 0x0097 [0x1C] WAIT(60* ticks)
 12: 0x009A [0x01] GOTO 0x00A8
 13: 0x009D [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00A8
 14: 0x00A5 [0x01] GOTO 0x00A8

SUBROUTINE_00A8:
 15: 0x00A8 [0x21] END_EVENT
 16: 0x00A9 [0x00] END_REQSTACK()
```

### Event 3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AA   |
| Data Size    | 23 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                37 06 80 07 80 08            7.....
00B0: 80 09 80 1F 00 0A 80 0B  80 08 80 1F 01 39 0C 80  .............9..
00C0: 00                                                .               
```

#### Opcodes

```
  0: 0x00AA [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-295.002*, z=15.083*, y=-143.621*, direction=224.2°*
  1: 0x00B3 [0x1F] MOVE_ENTITY: EventEntity moves to X=-299.697*, Z=19.497*, Y=-143.621*
  2: 0x00BB [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00BD [0x39] SET_ENTITY_DIRECTION(direction=14.0°*)
  4: 0x00C0 [0x00] END_REQSTACK()
```

### Event 4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C1   |
| Data Size    | 21 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:    32 0D 80 36 0E 80 0F  80 08 80 5A 00 0E 80 0F   2..6......Z....
00D0: 80 10 80 5A 01 00                                 ...Z..          
```

#### Opcodes

```
  0: 0x00C1 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00C4 [0x36] SET_ENTITY_EVENT_POSITION(pos_x=-299.757*, pos_z=19.874*, pos_y=-143.621*)
  2: 0x00CB [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-299.757*, Z=19.874*, Y=-116.113*
  3: 0x00D3 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  4: 0x00D5 [0x00] END_REQSTACK()
```

### Event 13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D6   |
| Data Size    | 23 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                   37 11  80 12 80 13 80 14 80 32        7........2
00E0: 0D 80 1F 00 15 80 16 80  17 80 1F 01 00           .............   
```

#### Opcodes

```
  0: 0x00D6 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-307.142*, z=21.258*, y=-116.051*, direction=198.6°*
  1: 0x00DF [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x00E2 [0x1F] MOVE_ENTITY: EventEntity moves to X=-311.285*, Z=22.720*, Y=-116.131*
  3: 0x00EA [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x00EC [0x00] END_REQSTACK()
```

### Event 5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00ED   |
| Data Size    | 94 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                         20 01 42                .B
00F0: 62 01 80 F0 FF FF 7F F0  FF FF 7F 6D 61 69 6E 02  b..........main.
0100: 80 1C 03 80 45 04 80 F0  FF FF 7F F0 FF FF 7F 66  ....E..........f
0110: 64 6F 31 02 80 1C 05 80  47 00 18 80 19 80 1A 80  do1.....G.......
0120: 1B 80 47 01 45 04 80 F0  FF FF 7F F0 FF FF 7F 66  ..G.E..........f
0130: 64 69 31 02 80 62 1C 80  F0 FF FF 7F F0 FF FF 7F  di1..b..........
0140: 6D 61 69 6E 02 80 1C 1D  80 21 00                 main.....!.     
```

#### Opcodes

```
  0: 0x00ED [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x00EF [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x00F0 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
  3: 0x0101 [0x1C] WAIT(140* ticks)
  4: 0x0104 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  5: 0x0115 [0x1C] WAIT(60* ticks)
  6: 0x0118 [0x47] UPDATE_PLAYER_POS(-311.436*, 22.886*, -116.139*, yaw=118.5°*)
  7: 0x0122 [0x47] WAIT_PLAYER_POS_UPDATE
  8: 0x0124 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  9: 0x0135 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[2*, 0*]
 10: 0x0146 [0x1C] WAIT(170* ticks)
 11: 0x0149 [0x21] END_EVENT
 12: 0x014A [0x00] END_REQSTACK()
```

### Event 7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x014B   |
| Data Size    | 57 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                                   20 01 42 45 04              .BE.
0150: 80 F0 FF FF 7F F0 FF FF  7F 66 64 6F 31 02 80 1C  .........fdo1...
0160: 05 80 47 00 1E 80 1F 80  20 80 21 80 47 01 45 04  ..G..... .!.G.E.
0170: 80 F0 FF FF 7F F0 FF FF  7F 66 64 69 31 02 80 1C  .........fdi1...
0180: 05 80 21 00                                       ..!.            
```

#### Opcodes

```
  0: 0x014B [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x014D [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x014E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  3: 0x015F [0x1C] WAIT(60* ticks)
  4: 0x0162 [0x47] UPDATE_PLAYER_POS(9.476*, 24.844*, -101.000*, yaw=88.4°*)
  5: 0x016C [0x47] WAIT_PLAYER_POS_UPDATE
  6: 0x016E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  7: 0x017F [0x1C] WAIT(60* ticks)
  8: 0x0182 [0x21] END_EVENT
  9: 0x0183 [0x00] END_REQSTACK()
```

### Event 8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0184   |
| Data Size    | 57 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:             20 01 42 45  04 80 F0 FF FF 7F F0 FF       .BE........
0190: FF 7F 66 64 6F 31 02 80  1C 05 80 47 00 22 80 23  ..fdo1.....G.".#
01A0: 80 24 80 25 80 47 01 45  04 80 F0 FF FF 7F F0 FF  .$.%.G.E........
01B0: FF 7F 66 64 69 31 02 80  1C 05 80 21 00           ..fdi1.....!.   
```

#### Opcodes

```
  0: 0x0184 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0186 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0187 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  3: 0x0198 [0x1C] WAIT(60* ticks)
  4: 0x019B [0x47] UPDATE_PLAYER_POS(-290.478*, 24.980*, -106.749*, yaw=77.7°*)
  5: 0x01A5 [0x47] WAIT_PLAYER_POS_UPDATE
  6: 0x01A7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  7: 0x01B8 [0x1C] WAIT(60* ticks)
  8: 0x01BB [0x21] END_EVENT
  9: 0x01BC [0x00] END_REQSTACK()
```

### Event 9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01BD   |
| Data Size    | 57 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:                                         20 01 42                .B
01C0: 45 04 80 F0 FF FF 7F F0  FF FF 7F 66 64 6F 31 02  E..........fdo1.
01D0: 80 1C 05 80 47 00 26 80  27 80 28 80 29 80 47 01  ....G.&.'.(.).G.
01E0: 45 04 80 F0 FF FF 7F F0  FF FF 7F 66 64 69 31 02  E..........fdi1.
01F0: 80 1C 05 80 21 00                                 ....!.          
```

#### Opcodes

```
  0: 0x01BD [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x01BF [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x01C0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  3: 0x01D1 [0x1C] WAIT(60* ticks)
  4: 0x01D4 [0x47] UPDATE_PLAYER_POS(249.357*, 24.912*, -37.000*, yaw=89.6°*)
  5: 0x01DE [0x47] WAIT_PLAYER_POS_UPDATE
  6: 0x01E0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  7: 0x01F1 [0x1C] WAIT(60* ticks)
  8: 0x01F4 [0x21] END_EVENT
  9: 0x01F5 [0x00] END_REQSTACK()
```

### Event 10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01F6   |
| Data Size    | 57 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01F0:                   20 01  42 45 04 80 F0 FF FF 7F         .BE......
0200: F0 FF FF 7F 66 64 6F 31  02 80 1C 05 80 47 00 2A  ....fdo1.....G.*
0210: 80 2B 80 2C 80 2D 80 47  01 45 04 80 F0 FF FF 7F  .+.,.-.G.E......
0220: F0 FF FF 7F 66 64 69 31  02 80 1C 05 80 21 00     ....fdi1.....!. 
```

#### Opcodes

```
  0: 0x01F6 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x01F8 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x01F9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  3: 0x020A [0x1C] WAIT(60* ticks)
  4: 0x020D [0x47] UPDATE_PLAYER_POS(30.333*, 25.118*, -42.749*, yaw=86.8°*)
  5: 0x0217 [0x47] WAIT_PLAYER_POS_UPDATE
  6: 0x0219 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  7: 0x022A [0x1C] WAIT(60* ticks)
  8: 0x022D [0x21] END_EVENT
  9: 0x022E [0x00] END_REQSTACK()
```

### Event 11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x022F   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0220:                                               47                 G
0230: 00 2E 80 2F 80 30 80 31  80 47 01 00              .../.0.1.G..    
```

#### Opcodes

```
  0: 0x022F [0x47] UPDATE_PLAYER_POS(317.664*, 20.082*, 16.000*, yaw=358.3°*)
  1: 0x0239 [0x47] WAIT_PLAYER_POS_UPDATE
  2: 0x023B [0x00] END_REQSTACK()
```

### Event 12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x023C   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0230:                                      32 0D 80 1F              2...
0240: 00 32 80 33 80 30 80 1F  01 00                    .2.3.0....      
```

#### Opcodes

```
  0: 0x023C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x023F [0x1F] MOVE_ENTITY: EventEntity moves to X=329.904*, Z=20.025*, Y=16.000*
  2: 0x0247 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0249 [0x00] END_REQSTACK()
```

### Event 14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x024A   |
| Data Size    | 50 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0240:                                4E 00 F0 FF FF 7F            N.....
0250: 20 01 42 80 F0 FF FF 7F  45 04 80 F0 FF FF 7F F0   .B.....E.......
0260: FF FF 7F 66 64 69 31 02  80 62 1C 80 F0 FF FF 7F  ...fdi1..b......
0270: F0 FF FF 7F 6D 61 69 6E  02 80 21 00              ....main..!.    
```

#### Opcodes

```
  0: 0x024A [0x4E] SET_ENTITY_HIDE_FLAG: Show LocalPlayer
  1: 0x0250 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  2: 0x0252 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  3: 0x0253 [0x80] LOAD_WAIT(entity=LocalPlayer)
  4: 0x0258 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  5: 0x0269 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[2*, 0*]
  6: 0x027A [0x21] END_EVENT
  7: 0x027B [0x00] END_REQSTACK()
```

### Event 18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x027C   |
| Data Size    | 88 bytes |
| Instructions | 22       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0270:                                      20 01 42 02               .B.
0280: 02 10 34 80 80 A7 02 24  35 80 01 80 02 80 25 02  ..4....$5.....%.
0290: 00 10 02 80 00 9F 02 03  01 10 34 80 01 A4 02 03  ..........4.....
02A0: 01 10 02 80 01 CF 02 02  02 10 04 80 80 CF 02 24  ...............$
02B0: 36 80 01 80 02 80 25 02  00 10 02 80 00 C7 02 03  6.....%.........
02C0: 01 10 04 80 01 CC 02 03  01 10 02 80 01 CF 02 2E  ................
02D0: 20 00 21 00                                        .!.            
```

#### Opcodes

```
  0: 0x027C [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x027E [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x027F [0x02] IF !(Work_Zone[2] == 100*) GOTO 0x02A7
  3: 0x0287 [0x24] CREATE_DIALOG(message_id=7383*, default_option=1*, option_flags=0*)
    → "Touch the crystal? [Yes./No.]"
  4: 0x028E [0x25] WAIT_DIALOG_SELECT()
  5: 0x028F [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x029F
  6: 0x0297 [0x03] Work_Zone[1] = 100*
  7: 0x029C [0x01] GOTO 0x02A4
  8: 0x029F [0x03] Work_Zone[1] = 0*

SUBROUTINE_02A4:
  9: 0x02A4 [0x01] GOTO 0x02CF
 10: 0x02A7 [0x02] IF !(Work_Zone[2] == 200*) GOTO 0x02CF
 11: 0x02AF [0x24] CREATE_DIALOG(message_id=7380*, default_option=1*, option_flags=0*)
    → "Touch the crystal? [Yes./No.]"
 12: 0x02B6 [0x25] WAIT_DIALOG_SELECT()
 13: 0x02B7 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x02C7
 14: 0x02BF [0x03] Work_Zone[1] = 200*
 15: 0x02C4 [0x01] GOTO 0x02CC
 16: 0x02C7 [0x03] Work_Zone[1] = 0*

SUBROUTINE_02CC:
 17: 0x02CC [0x01] GOTO 0x02CF

SUBROUTINE_02CF:
 18: 0x02CF [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
 19: 0x02D0 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 20: 0x02D2 [0x21] END_EVENT
 21: 0x02D3 [0x00] END_REQSTACK()
```
