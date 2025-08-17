# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Uleguerand Range (ID: 5) |
| Block Size       | 896 bytes                |
| Total Events     | 14                       |
| References Count | 47                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65534](#event-65534)    | 0x0001       |      1 |              1 |
| [2](#event-2)            | 0x0002       |    165 |             29 |
| [3](#event-3)            | 0x00A7       |    165 |             29 |
| [4](#event-4)            | 0x014C       |    165 |             29 |
| [65535.1](#event-655351) | 0x01F1       |      6 |              2 |
| [65535.2](#event-655352) | 0x01F7       |      6 |              2 |
| [65535.3](#event-655353) | 0x01FD       |      6 |              2 |
| [65535.4](#event-655354) | 0x0203       |     10 |              2 |
| [65535.5](#event-655355) | 0x020D       |     10 |              2 |
| [65535.6](#event-655356) | 0x0217       |      6 |              2 |
| [65535.7](#event-655357) | 0x021D       |     50 |             12 |
| [65535.8](#event-655358) | 0x024F       |     29 |              4 |
| [65535.9](#event-655359) | 0x026C       |     15 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1CAC      |        7340 |
|       1 | 0x0001      |           1 |
|       2 | 0x0000      |           0 |
|       3 | 0x0078      |         120 |
|       4 | 0x005A      |          90 |
|       5 | 0x004D      |          77 |
|       6 | 0x00B4      |         180 |
|       7 | 0x00C8      |         200 |
|       8 | 0x003C      |          60 |
|       9 | 0x5CFDC     |      380892 |
|      10 | 0xFFFD5179  |  4294791545 |
|      11 | 0xFFFFF588  |  4294964616 |
|      12 | 0x0C00      |        3072 |
|      13 | 0x0014      |          20 |
|      14 | 0x004E      |          78 |
|      15 | 0x0002      |           2 |
|      16 | 0x709BD     |      461245 |
|      17 | 0x36CC9     |      224457 |
|      18 | 0xFFFEFD50  |  4294901072 |
|      19 | 0x2AC1F     |      175135 |
|      20 | 0x79D28     |      498984 |
|      21 | 0xFFFE4156  |  4294852950 |
|      22 | 0x0800      |        2048 |
|      23 | 0xFFFB72C9  |  4294669001 |
|      24 | 0xFFFFB37A  |  4294947706 |
|      25 | 0xFFFF3577  |  4294915447 |
|      26 | 0x040E      |        1038 |
|      27 | 0xFFFB73EB  |  4294669291 |
|      28 | 0xFFF760AF  |  4294402223 |
|      29 | 0xFFFF6451  |  4294927441 |
|      30 | 0x0CC5      |        3269 |
|      31 | 0x0026      |          38 |
|      32 | 0xFFFB7995  |  4294670741 |
|      33 | 0xFFF78110  |  4294410512 |
|      34 | 0xFFFF63E8  |  4294927336 |
|      35 | 0x0FCC      |        4044 |
|      36 | 0x001E      |          30 |
|      37 | 0x0966      |        2406 |
|      38 | 0x002D      |          45 |
|      39 | 0xFFFBA4DA  |  4294681818 |
|      40 | 0xFFF7B8A8  |  4294424744 |
|      41 | 0xFFFF642B  |  4294927403 |
|      42 | 0x0DE0      |        3552 |
|      43 | 0x000A      |          10 |
|      44 | 0xFFFBAA34  |  4294683188 |
|      45 | 0xFFF7BFB5  |  4294426549 |
|      46 | 0xFFFF64B3  |  4294927539 |

## String References

- **7340**: Use the $3? [Yes./No.]

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

### Event 2

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0002    |
| Data Size    | 165 bytes |
| Instructions | 29        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       24 00 80 01 80 02  80 25 02 00 10 02 80 00    $......%......
0010: 93 00 20 01 42 1C 03 80  43 00 43 01 2D F8 FF FF  .. .B...C.C.-...
0020: 7F F8 FF FF 7F 74 61 74  31 1C 04 80 9F 05 80 F8  .....tat1.......
0030: FF FF 7F F8 FF FF 7F 6D  61 69 6E 02 80 1C 06 80  .......main.....
0040: 45 07 80 F0 FF FF 7F F0  FF FF 7F 66 64 6F 31 02  E..........fdo1.
0050: 80 1C 08 80 47 00 09 80  0A 80 0B 80 0C 80 47 01  ....G.........G.
0060: 1C 0D 80 45 07 80 F0 FF  FF 7F F0 FF FF 7F 66 64  ...E..........fd
0070: 69 31 02 80 1C 08 80 9F  0E 80 F8 FF FF 7F F8 FF  i1..............
0080: FF 7F 6D 61 69 6E 02 80  1C 03 80 03 01 10 0F 80  ..main..........
0090: 01 A3 00 02 00 10 01 80  00 A3 00 03 01 10 01 80  ................
00A0: 01 A3 00 20 00 21 00                              ... .!.         
```

#### Opcodes

```
  0: 0x0002 [0x24] CREATE_DIALOG(message_id=7340*, default_option=1*, option_flags=0*)
    → "Use the $3? [Yes./No.]"
  1: 0x0009 [0x25] WAIT_DIALOG_SELECT()
  2: 0x000A [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0093
  3: 0x0012 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  4: 0x0014 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x0015 [0x1C] WAIT(120* ticks)
  6: 0x0018 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  7: 0x001A [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  8: 0x001C [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "tat1" with entities [EventEntity, EventEntity]
  9: 0x0029 [0x1C] WAIT(90* ticks)
 10: 0x002C [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [EventEntity, EventEntity], work=[77*, 0*]
 11: 0x003D [0x1C] WAIT(180* ticks)
 12: 0x0040 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 13: 0x0051 [0x1C] WAIT(60* ticks)
 14: 0x0054 [0x47] UPDATE_PLAYER_POS(380.892*, -175.751*, -2.680*, yaw=270.0°*)
 15: 0x005E [0x47] WAIT_PLAYER_POS_UPDATE
 16: 0x0060 [0x1C] WAIT(20* ticks)
 17: 0x0063 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 18: 0x0074 [0x1C] WAIT(60* ticks)
 19: 0x0077 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [EventEntity, EventEntity], work=[78*, 0*]
 20: 0x0088 [0x1C] WAIT(120* ticks)
 21: 0x008B [0x03] Work_Zone[1] = 2*
 22: 0x0090 [0x01] GOTO 0x00A3
 23: 0x0093 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00A3
 24: 0x009B [0x03] Work_Zone[1] = 1*
 25: 0x00A0 [0x01] GOTO 0x00A3

SUBROUTINE_00A3:
 26: 0x00A3 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 27: 0x00A5 [0x21] END_EVENT
 28: 0x00A6 [0x00] END_REQSTACK()
```

### Event 3

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00A7    |
| Data Size    | 165 bytes |
| Instructions | 29        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                      24  00 80 01 80 02 80 25 02         $......%.
00B0: 00 10 02 80 00 38 01 20  01 42 1C 03 80 43 00 43  .....8. .B...C.C
00C0: 01 2D F8 FF FF 7F F8 FF  FF 7F 74 61 74 32 1C 04  .-........tat2..
00D0: 80 9F 05 80 F8 FF FF 7F  F8 FF FF 7F 6D 61 69 6E  ............main
00E0: 02 80 1C 06 80 45 07 80  F0 FF FF 7F F0 FF FF 7F  .....E..........
00F0: 66 64 6F 31 02 80 1C 08  80 47 00 10 80 11 80 12  fdo1.....G......
0100: 80 0C 80 47 01 1C 0D 80  45 07 80 F0 FF FF 7F F0  ...G....E.......
0110: FF FF 7F 66 64 69 31 02  80 1C 08 80 9F 0E 80 F8  ...fdi1.........
0120: FF FF 7F F8 FF FF 7F 6D  61 69 6E 02 80 1C 03 80  .......main.....
0130: 03 01 10 0F 80 01 48 01  02 00 10 01 80 00 48 01  ......H.......H.
0140: 03 01 10 01 80 01 48 01  20 00 21 00              ......H. .!.    
```

#### Opcodes

```
  0: 0x00A7 [0x24] CREATE_DIALOG(message_id=7340*, default_option=1*, option_flags=0*)
    → "Use the $3? [Yes./No.]"
  1: 0x00AE [0x25] WAIT_DIALOG_SELECT()
  2: 0x00AF [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0138
  3: 0x00B7 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  4: 0x00B9 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x00BA [0x1C] WAIT(120* ticks)
  6: 0x00BD [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  7: 0x00BF [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  8: 0x00C1 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "tat2" with entities [EventEntity, EventEntity]
  9: 0x00CE [0x1C] WAIT(90* ticks)
 10: 0x00D1 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [EventEntity, EventEntity], work=[77*, 0*]
 11: 0x00E2 [0x1C] WAIT(180* ticks)
 12: 0x00E5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 13: 0x00F6 [0x1C] WAIT(60* ticks)
 14: 0x00F9 [0x47] UPDATE_PLAYER_POS(461.245*, 224.457*, -66.224*, yaw=270.0°*)
 15: 0x0103 [0x47] WAIT_PLAYER_POS_UPDATE
 16: 0x0105 [0x1C] WAIT(20* ticks)
 17: 0x0108 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 18: 0x0119 [0x1C] WAIT(60* ticks)
 19: 0x011C [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [EventEntity, EventEntity], work=[78*, 0*]
 20: 0x012D [0x1C] WAIT(120* ticks)
 21: 0x0130 [0x03] Work_Zone[1] = 2*
 22: 0x0135 [0x01] GOTO 0x0148
 23: 0x0138 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0148
 24: 0x0140 [0x03] Work_Zone[1] = 1*
 25: 0x0145 [0x01] GOTO 0x0148

SUBROUTINE_0148:
 26: 0x0148 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 27: 0x014A [0x21] END_EVENT
 28: 0x014B [0x00] END_REQSTACK()
```

### Event 4

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x014C    |
| Data Size    | 165 bytes |
| Instructions | 29        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                                      24 00 80 01              $...
0150: 80 02 80 25 02 00 10 02  80 00 DD 01 20 01 42 1C  ...%........ .B.
0160: 03 80 43 00 43 01 2D F8  FF FF 7F F8 FF FF 7F 74  ..C.C.-........t
0170: 61 74 33 1C 04 80 9F 05  80 F8 FF FF 7F F8 FF FF  at3.............
0180: 7F 6D 61 69 6E 02 80 1C  06 80 45 07 80 F0 FF FF  .main.....E.....
0190: 7F F0 FF FF 7F 66 64 6F  31 02 80 1C 08 80 47 00  .....fdo1.....G.
01A0: 13 80 14 80 15 80 16 80  47 01 1C 0D 80 45 07 80  ........G....E..
01B0: F0 FF FF 7F F0 FF FF 7F  66 64 69 31 02 80 1C 08  ........fdi1....
01C0: 80 9F 0E 80 F8 FF FF 7F  F8 FF FF 7F 6D 61 69 6E  ............main
01D0: 02 80 1C 03 80 03 01 10  0F 80 01 ED 01 02 00 10  ................
01E0: 01 80 00 ED 01 03 01 10  01 80 01 ED 01 20 00 21  ............. .!
01F0: 00                                                .               
```

#### Opcodes

```
  0: 0x014C [0x24] CREATE_DIALOG(message_id=7340*, default_option=1*, option_flags=0*)
    → "Use the $3? [Yes./No.]"
  1: 0x0153 [0x25] WAIT_DIALOG_SELECT()
  2: 0x0154 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01DD
  3: 0x015C [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  4: 0x015E [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x015F [0x1C] WAIT(120* ticks)
  6: 0x0162 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  7: 0x0164 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  8: 0x0166 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "tat3" with entities [EventEntity, EventEntity]
  9: 0x0173 [0x1C] WAIT(90* ticks)
 10: 0x0176 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [EventEntity, EventEntity], work=[77*, 0*]
 11: 0x0187 [0x1C] WAIT(180* ticks)
 12: 0x018A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 13: 0x019B [0x1C] WAIT(60* ticks)
 14: 0x019E [0x47] UPDATE_PLAYER_POS(175.135*, 498.984*, -114.346*, yaw=180.0°*)
 15: 0x01A8 [0x47] WAIT_PLAYER_POS_UPDATE
 16: 0x01AA [0x1C] WAIT(20* ticks)
 17: 0x01AD [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 18: 0x01BE [0x1C] WAIT(60* ticks)
 19: 0x01C1 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [EventEntity, EventEntity], work=[78*, 0*]
 20: 0x01D2 [0x1C] WAIT(120* ticks)
 21: 0x01D5 [0x03] Work_Zone[1] = 2*
 22: 0x01DA [0x01] GOTO 0x01ED
 23: 0x01DD [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x01ED
 24: 0x01E5 [0x03] Work_Zone[1] = 1*
 25: 0x01EA [0x01] GOTO 0x01ED

SUBROUTINE_01ED:
 26: 0x01ED [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 27: 0x01EF [0x21] END_EVENT
 28: 0x01F0 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01F1  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01F0:    03 02 10 0B 7F 00                               ......         
```

#### Opcodes

```
  0: 0x01F1 [0x03] Work_Zone[2] = (Entity->Render.Flags01 >> 25) & 1
  1: 0x01F6 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01F7  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01F0:                      03  09 10 07 7F 00                  ......   
```

#### Opcodes

```
  0: 0x01F7 [0x03] Work_Zone[9] = Entity->Race
  1: 0x01FC [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01FD  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01F0:                                         03 02 10               ...
0200: 06 7F 00                                          ...             
```

#### Opcodes

```
  0: 0x01FD [0x03] Work_Zone[2] = Entity->JobId (if LocalPlayer)
  1: 0x0202 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0203   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0200:          37 17 80 18 80  19 80 1A 80 00              7.........   
```

#### Opcodes

```
  0: 0x0203 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-298.295*, z=-19.590*, y=-51.849*, direction=91.2°*
  1: 0x020C [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x020D   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0200:                                         37 1B 80               7..
0210: 1C 80 1D 80 1E 80 00                              .......         
```

#### Opcodes

```
  0: 0x020D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-298.005*, z=-565.073*, y=-39.855*, direction=287.3°*
  1: 0x0216 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0217  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0210:                      03  02 10 0B 7F 00                  ......   
```

#### Opcodes

```
  0: 0x0217 [0x03] Work_Zone[2] = (Entity->Render.Flags01 >> 25) & 1
  1: 0x021C [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x021D   |
| Data Size    | 50 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0210:                                         32 1F 80               2..
0220: 1F 00 20 80 21 80 22 80  1F 01 6F 4B F8 FF FF 7F  .. .!."...oK....
0230: 23 80 1C 24 80 4B F8 FF  FF 7F 25 80 1C 26 80 4A  #..$.K....%..&.J
0240: F8 FF FF 7F BE 51 00 01  6F 76 F8 FF FF 7F 00     .....Q..ov..... 
```

#### Opcodes

```
  0: 0x021D [0x32] ExtData[1]->MainSpeed = 38* * 0.1
  1: 0x0220 [0x1F] MOVE_ENTITY: EventEntity moves to X=-296.555*, Z=-556.784*, Y=-39.960*
  2: 0x0228 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x022A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x022B [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=22.2°*)
  5: 0x0232 [0x1C] WAIT(30* ticks)
  6: 0x0235 [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=13.2°*)
  7: 0x023C [0x1C] WAIT(45* ticks)
  8: 0x023F [0x4A] EventEntity looks at Louverance (ID: 16798142/0x010051BE)
  9: 0x0248 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 10: 0x0249 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
 11: 0x024E [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x024F   |
| Data Size    | 29 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0240:                                               79                 y
0250: 00 F8 FF FF 7F BD 51 00  01 6C F8 FF FF 7F 02 80  ......Q..l......
0260: 01 80 37 27 80 28 80 29  80 2A 80 00              ..7'.(.).*..    
```

#### Opcodes

```
  0: 0x024F [0x79] EventEntity looks at Louverance (ID: 16798141/0x010051BD) (Basic look)
  1: 0x0259 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  2: 0x0262 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-285.478*, z=-542.552*, y=-39.893*, direction=312.2°*
  3: 0x026B [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x026C   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0260:                                      32 2B 80 1F              2+..
0270: 00 2C 80 2D 80 2E 80 1F  01 6F 00                 .,.-.....o.     
```

#### Opcodes

```
  0: 0x026C [0x32] ExtData[1]->MainSpeed = 10* * 0.1
  1: 0x026F [0x1F] MOVE_ENTITY: EventEntity moves to X=-284.108*, Z=-540.747*, Y=-39.757*
  2: 0x0277 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0279 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x027A [0x00] END_REQSTACK()
```
