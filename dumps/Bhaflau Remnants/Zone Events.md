# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Bhaflau Remnants (ID: 75) |
| Block Size       | 2028 bytes                |
| Total Events     | 23                        |
| References Count | 41                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [65534](#event-65534) | 0x0001       |      1 |              1 |
| [0](#event-0)         | 0x0002       |     26 |              7 |
| [1](#event-1)         | 0x001C       |     46 |              9 |
| [50](#event-50)       | 0x004A       |     41 |              5 |
| [51](#event-51)       | 0x0073       |     38 |              4 |
| [100](#event-100)     | 0x0099       |     55 |             11 |
| [101](#event-101)     | 0x00D0       |     55 |             11 |
| [4](#event-4)         | 0x0107       |    108 |             16 |
| [5](#event-5)         | 0x0173       |     84 |             12 |
| [200](#event-200)     | 0x01C7       |     72 |             18 |
| [201](#event-201)     | 0x020F       |     72 |             18 |
| [202](#event-202)     | 0x0257       |     72 |             18 |
| [203](#event-203)     | 0x029F       |     72 |             18 |
| [204](#event-204)     | 0x02E7       |     72 |             18 |
| [205](#event-205)     | 0x032F       |     72 |             18 |
| [206](#event-206)     | 0x0377       |     72 |             18 |
| [207](#event-207)     | 0x03BF       |     79 |             19 |
| [208](#event-208)     | 0x040E       |     46 |             14 |
| [209](#event-209)     | 0x043C       |     79 |             19 |
| [300](#event-300)     | 0x048B       |     31 |             10 |
| [2](#event-2)         | 0x04AA       |    526 |             86 |
| [3](#event-3)         | 0x06B8       |     35 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C8      |         200 |
|       1 | 0x0000      |           0 |
|       2 | 0x003C      |          60 |
|       3 | 0x00C9      |         201 |
|       4 | 0x008C      |         140 |
|       5 | 0x00CA      |         202 |
|       6 | 0x00E7      |         231 |
|       7 | 0x00AA      |         170 |
|       8 | 0x001E      |          30 |
|       9 | 0x0078      |         120 |
|      10 | 0x1D10      |        7440 |
|      11 | 0x0001      |           1 |
|      12 | 0x53020     |      340000 |
|      13 | 0x222E0     |      140000 |
|      14 | 0xFFFFFE0D  |  4294966797 |
|      15 | 0x0C00      |        3072 |
|      16 | 0xFFF99760  |  4294547296 |
|      17 | 0xFFFACFE0  |  4294627296 |
|      18 | 0x0800      |        2048 |
|      19 | 0xFFFA33A0  |  4294587296 |
|      20 | 0xFFF72660  |  4294387296 |
|      21 | 0xFFFC0860  |  4294707296 |
|      22 | 0xFFFFFE0C  |  4294966796 |
|      23 | 0xFFFB6C20  |  4294667296 |
|      24 | 0xFFF8FB20  |  4294507296 |
|      25 | 0xFFFFB1E0  |  4294947296 |
|      26 | 0xFFFCA4A0  |  4294747296 |
|      27 | 0x1D12      |        7442 |
|      28 | 0x000F      |          15 |
|      29 | 0x0010      |          16 |
|      30 | 0x001F      |          31 |
|      31 | 0x0002      |           2 |
|      32 | 0x0003      |           3 |
|      33 | 0x0004      |           4 |
|      34 | 0x0005      |           5 |
|      35 | 0x0006      |           6 |
|      36 | 0x0007      |           7 |
|      37 | 0x0008      |           8 |
|      38 | 0xFFFFFFFF  |  4294967295 |
|      39 | 0x1C4F      |        7247 |
|      40 | 0x1D14      |        7444 |

## String References

- **7247**: What do you take? [Nothing./$1 ($2 remaining)/$3 ($4 remaining)/$5 ($6 remaining)/$7 ($8 remaining)/$9 ($10 remaining)/$11 ($12 remaining)/$13 ($14 remaining)/$15 ($16 remaining)]
- **7440**: Use the device? [Yes./No.]
- **7442**: Open the door? [Yes./No.]
- **7444**: Open the gate? [Yes./No.]

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
| Data Size    | 26 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       20 01 42 45 00 80  F0 FF FF 7F F0 FF FF 7F     .BE..........
0010: 66 64 6F 31 01 80 1C 02  80 30 21 00              fdo1.....0!.    
```

#### Opcodes

```
  0: 0x0002 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0004 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0005 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  3: 0x0016 [0x1C] WAIT(60* ticks)
  4: 0x0019 [0x30] SET_UCOFF_CONTINUE_ZERO()
  5: 0x001A [0x21] END_EVENT
  6: 0x001B [0x00] END_REQSTACK()
```

### Event 1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001C   |
| Data Size    | 46 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                      20 01 42 9F               .B.
0020: 03 80 F8 FF FF 7F F8 FF  FF 7F 6D 61 69 6E 01 80  ..........main..
0030: 1C 04 80 45 00 80 F0 FF  FF 7F F0 FF FF 7F 66 64  ...E..........fd
0040: 6F 31 01 80 1C 02 80 30  21 00                    o1.....0!.      
```

#### Opcodes

```
  0: 0x001C [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x001E [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x001F [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [EventEntity, EventEntity], work=[201*, 0*]
  3: 0x0030 [0x1C] WAIT(140* ticks)
  4: 0x0033 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  5: 0x0044 [0x1C] WAIT(60* ticks)
  6: 0x0047 [0x30] SET_UCOFF_CONTINUE_ZERO()
  7: 0x0048 [0x21] END_EVENT
  8: 0x0049 [0x00] END_REQSTACK()
```

### Event 50

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004A   |
| Data Size    | 41 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                9F 05 80 F8 FF FF            ......
0050: 7F F8 FF FF 7F 6D 61 69  6E 01 80 1C 04 80 45 00  .....main.....E.
0060: 80 F0 FF FF 7F F0 FF FF  7F 66 64 6F 31 01 80 1C  .........fdo1...
0070: 02 80 00                                          ...             
```

#### Opcodes

```
  0: 0x004A [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [EventEntity, EventEntity], work=[202*, 0*]
  1: 0x005B [0x1C] WAIT(140* ticks)
  2: 0x005E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  3: 0x006F [0x1C] WAIT(60* ticks)
  4: 0x0072 [0x00] END_REQSTACK()
```

### Event 51

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0073   |
| Data Size    | 38 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:          45 00 80 F0 FF  FF 7F F0 FF FF 7F 66 64     E..........fd
0080: 69 31 01 80 9F 06 80 F8  FF FF 7F F8 FF FF 7F 6D  i1.............m
0090: 61 69 6E 01 80 1C 07 80  00                       ain......       
```

#### Opcodes

```
  0: 0x0073 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  1: 0x0084 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [EventEntity, EventEntity], work=[231*, 0*]
  2: 0x0095 [0x1C] WAIT(170* ticks)
  3: 0x0098 [0x00] END_REQSTACK()
```

### Event 100

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0099   |
| Data Size    | 55 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                             20 01 42 43 00 43 01            .BC.C.
00A0: 45 00 80 F0 FF FF 7F F0  FF FF 7F 66 64 6F 31 01  E..........fdo1.
00B0: 80 1C 02 80 29 01 FC B1  04 01 01 45 00 80 F0 FF  ....)......E....
00C0: FF 7F F0 FF FF 7F 66 64  69 31 01 80 20 00 21 00  ......fdi1.. .!.
```

#### Opcodes

```
  0: 0x0099 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x009B [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x009C [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  3: 0x009E [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  4: 0x00A0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  5: 0x00B1 [0x1C] WAIT(60* ticks)
  6: 0x00B4 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Weather (ID: 17084924/0x0104B1FC), tag_num=0x01)
  7: 0x00BB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  8: 0x00CC [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  9: 0x00CE [0x21] END_EVENT
 10: 0x00CF [0x00] END_REQSTACK()
```

### Event 101

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D0   |
| Data Size    | 55 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0: 20 01 42 43 00 43 01 45  00 80 F0 FF FF 7F F0 FF   .BC.C.E........
00E0: FF 7F 66 64 6F 31 01 80  1C 02 80 29 01 FC B1 04  ..fdo1.....)....
00F0: 01 02 45 00 80 F0 FF FF  7F F0 FF FF 7F 66 64 69  ..E..........fdi
0100: 31 01 80 20 00 21 00                              1.. .!.         
```

#### Opcodes

```
  0: 0x00D0 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x00D2 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x00D3 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  3: 0x00D5 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  4: 0x00D7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  5: 0x00E8 [0x1C] WAIT(60* ticks)
  6: 0x00EB [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Weather (ID: 17084924/0x0104B1FC), tag_num=0x02)
  7: 0x00F2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  8: 0x0103 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  9: 0x0105 [0x21] END_EVENT
 10: 0x0106 [0x00] END_REQSTACK()
```

### Event 4

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0107    |
| Data Size    | 108 bytes |
| Instructions | 16        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                      42  9F 05 80 F8 FF FF 7F F8         B........
0110: FF FF 7F 6D 61 69 6E 01  80 1C 04 80 45 00 80 F0  ...main.....E...
0120: FF FF 7F F0 FF FF 7F 66  64 6F 31 01 80 1C 02 80  .......fdo1.....
0130: 3E 02 10 08 80 41 01 29  01 FC B1 04 01 01 01 48  >....A.).......H
0140: 01 29 01 FC B1 04 01 02  43 00 43 01 45 00 80 F0  .)......C.C.E...
0150: FF FF 7F F0 FF FF 7F 66  64 69 31 01 80 9F 06 80  .......fdi1.....
0160: F8 FF FF 7F F8 FF FF 7F  6D 61 69 6E 01 80 1C 09  ........main....
0170: 80 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x0107 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0108 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [EventEntity, EventEntity], work=[202*, 0*]
  2: 0x0119 [0x1C] WAIT(140* ticks)
  3: 0x011C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x012D [0x1C] WAIT(60* ticks)
  5: 0x0130 [0x3E] IF !(Work_Zone[2] bit 30*) GOTO 0x0141
  6: 0x0137 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Weather (ID: 17084924/0x0104B1FC), tag_num=0x01)
  7: 0x013E [0x01] GOTO 0x0148
  8: 0x0141 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Weather (ID: 17084924/0x0104B1FC), tag_num=0x02)

SUBROUTINE_0148:
  9: 0x0148 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 10: 0x014A [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 11: 0x014C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 12: 0x015D [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [EventEntity, EventEntity], work=[231*, 0*]
 13: 0x016E [0x1C] WAIT(120* ticks)
 14: 0x0171 [0x21] END_EVENT
 15: 0x0172 [0x00] END_REQSTACK()
```

### Event 5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0173   |
| Data Size    | 84 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:          42 9F 05 80 F8  FF FF 7F F8 FF FF 7F 6D     B...........m
0180: 61 69 6E 01 80 1C 04 80  45 00 80 F0 FF FF 7F F0  ain.....E.......
0190: FF FF 7F 66 64 6F 31 01  80 1C 02 80 43 00 43 01  ...fdo1.....C.C.
01A0: 45 00 80 F0 FF FF 7F F0  FF FF 7F 66 64 69 31 01  E..........fdi1.
01B0: 80 9F 06 80 F8 FF FF 7F  F8 FF FF 7F 6D 61 69 6E  ............main
01C0: 01 80 1C 09 80 21 00                              .....!.         
```

#### Opcodes

```
  0: 0x0173 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0174 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [EventEntity, EventEntity], work=[202*, 0*]
  2: 0x0185 [0x1C] WAIT(140* ticks)
  3: 0x0188 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x0199 [0x1C] WAIT(60* ticks)
  5: 0x019C [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  6: 0x019E [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  7: 0x01A0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  8: 0x01B1 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [EventEntity, EventEntity], work=[231*, 0*]
  9: 0x01C2 [0x1C] WAIT(120* ticks)
 10: 0x01C5 [0x21] END_EVENT
 11: 0x01C6 [0x00] END_REQSTACK()
```

### Event 200

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01C7   |
| Data Size    | 72 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0:                      20  01 24 0A 80 0B 80 01 80          .$......
01D0: 25 02 00 10 01 80 00 00  02 42 43 00 43 01 03 01  %........BC.C...
01E0: 10 0B 80 29 01 F0 FF FF  7F 04 47 00 0C 80 0D 80  ...)......G.....
01F0: 0E 80 0F 80 47 01 29 01  F0 FF FF 7F 05 01 0B 02  ....G.).........
0200: 02 00 10 0B 80 00 0B 02  01 0B 02 20 00 21 00     ........... .!. 
```

#### Opcodes

```
  0: 0x01C7 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x01C9 [0x24] CREATE_DIALOG(message_id=7440*, default_option=1*, option_flags=0*)
    → "Use the device? [Yes./No.]"
  2: 0x01D0 [0x25] WAIT_DIALOG_SELECT()
  3: 0x01D1 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0200
  4: 0x01D9 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x01DA [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  6: 0x01DC [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  7: 0x01DE [0x03] Work_Zone[1] = 1*
  8: 0x01E3 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
  9: 0x01EA [0x47] UPDATE_PLAYER_POS(340.000*, 140.000*, -0.499*, yaw=270.0°*)
 10: 0x01F4 [0x47] WAIT_PLAYER_POS_UPDATE
 11: 0x01F6 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x05)
 12: 0x01FD [0x01] GOTO 0x020B
 13: 0x0200 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x020B
 14: 0x0208 [0x01] GOTO 0x020B

SUBROUTINE_020B:
 15: 0x020B [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 16: 0x020D [0x21] END_EVENT
 17: 0x020E [0x00] END_REQSTACK()
```

### Event 201

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x020F   |
| Data Size    | 72 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0200:                                               20                  
0210: 01 24 0A 80 0B 80 01 80  25 02 00 10 01 80 00 48  .$......%......H
0220: 02 42 43 00 43 01 03 01  10 0B 80 29 01 F0 FF FF  .BC.C......)....
0230: 7F 04 47 00 10 80 11 80  01 80 12 80 47 01 29 01  ..G.........G.).
0240: F0 FF FF 7F 05 01 53 02  02 00 10 0B 80 00 53 02  ......S.......S.
0250: 01 53 02 20 00 21 00                              .S. .!.         
```

#### Opcodes

```
  0: 0x020F [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0211 [0x24] CREATE_DIALOG(message_id=7440*, default_option=1*, option_flags=0*)
    → "Use the device? [Yes./No.]"
  2: 0x0218 [0x25] WAIT_DIALOG_SELECT()
  3: 0x0219 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0248
  4: 0x0221 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x0222 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  6: 0x0224 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  7: 0x0226 [0x03] Work_Zone[1] = 1*
  8: 0x022B [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
  9: 0x0232 [0x47] UPDATE_PLAYER_POS(-420.000*, -340.000*, 0.000*, yaw=180.0°*)
 10: 0x023C [0x47] WAIT_PLAYER_POS_UPDATE
 11: 0x023E [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x05)
 12: 0x0245 [0x01] GOTO 0x0253
 13: 0x0248 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0253
 14: 0x0250 [0x01] GOTO 0x0253

SUBROUTINE_0253:
 15: 0x0253 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 16: 0x0255 [0x21] END_EVENT
 17: 0x0256 [0x00] END_REQSTACK()
```

### Event 202

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0257   |
| Data Size    | 72 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0250:                      20  01 24 0A 80 0B 80 01 80          .$......
0260: 25 02 00 10 01 80 00 90  02 42 43 00 43 01 03 01  %........BC.C...
0270: 10 0B 80 29 01 F0 FF FF  7F 04 47 00 13 80 14 80  ...)......G.....
0280: 0E 80 12 80 47 01 29 01  F0 FF FF 7F 05 01 9B 02  ....G.).........
0290: 02 00 10 0B 80 00 9B 02  01 9B 02 20 00 21 00     ........... .!. 
```

#### Opcodes

```
  0: 0x0257 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0259 [0x24] CREATE_DIALOG(message_id=7440*, default_option=1*, option_flags=0*)
    → "Use the device? [Yes./No.]"
  2: 0x0260 [0x25] WAIT_DIALOG_SELECT()
  3: 0x0261 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0290
  4: 0x0269 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x026A [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  6: 0x026C [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  7: 0x026E [0x03] Work_Zone[1] = 1*
  8: 0x0273 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
  9: 0x027A [0x47] UPDATE_PLAYER_POS(-380.000*, -580.000*, -0.499*, yaw=180.0°*)
 10: 0x0284 [0x47] WAIT_PLAYER_POS_UPDATE
 11: 0x0286 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x05)
 12: 0x028D [0x01] GOTO 0x029B
 13: 0x0290 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x029B
 14: 0x0298 [0x01] GOTO 0x029B

SUBROUTINE_029B:
 15: 0x029B [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 16: 0x029D [0x21] END_EVENT
 17: 0x029E [0x00] END_REQSTACK()
```

### Event 203

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x029F   |
| Data Size    | 72 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0290:                                               20                  
02A0: 01 24 0A 80 0B 80 01 80  25 02 00 10 01 80 00 D8  .$......%.......
02B0: 02 42 43 00 43 01 03 01  10 0B 80 29 01 F0 FF FF  .BC.C......)....
02C0: 7F 04 47 00 15 80 11 80  16 80 01 80 47 01 29 01  ..G.........G.).
02D0: F0 FF FF 7F 05 01 E3 02  02 00 10 0B 80 00 E3 02  ................
02E0: 01 E3 02 20 00 21 00                              ... .!.         
```

#### Opcodes

```
  0: 0x029F [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x02A1 [0x24] CREATE_DIALOG(message_id=7440*, default_option=1*, option_flags=0*)
    → "Use the device? [Yes./No.]"
  2: 0x02A8 [0x25] WAIT_DIALOG_SELECT()
  3: 0x02A9 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x02D8
  4: 0x02B1 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x02B2 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  6: 0x02B4 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  7: 0x02B6 [0x03] Work_Zone[1] = 1*
  8: 0x02BB [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
  9: 0x02C2 [0x47] UPDATE_PLAYER_POS(-260.000*, -340.000*, -0.500*, yaw=0.0°*)
 10: 0x02CC [0x47] WAIT_PLAYER_POS_UPDATE
 11: 0x02CE [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x05)
 12: 0x02D5 [0x01] GOTO 0x02E3
 13: 0x02D8 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x02E3
 14: 0x02E0 [0x01] GOTO 0x02E3

SUBROUTINE_02E3:
 15: 0x02E3 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 16: 0x02E5 [0x21] END_EVENT
 17: 0x02E6 [0x00] END_REQSTACK()
```

### Event 204

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x02E7   |
| Data Size    | 72 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02E0:                      20  01 24 0A 80 0B 80 01 80          .$......
02F0: 25 02 00 10 01 80 00 20  03 42 43 00 43 01 03 01  %...... .BC.C...
0300: 10 0B 80 29 01 F0 FF FF  7F 04 47 00 17 80 14 80  ...)......G.....
0310: 0E 80 01 80 47 01 29 01  F0 FF FF 7F 05 01 2B 03  ....G.).......+.
0320: 02 00 10 0B 80 00 2B 03  01 2B 03 20 00 21 00     ......+..+. .!. 
```

#### Opcodes

```
  0: 0x02E7 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x02E9 [0x24] CREATE_DIALOG(message_id=7440*, default_option=1*, option_flags=0*)
    → "Use the device? [Yes./No.]"
  2: 0x02F0 [0x25] WAIT_DIALOG_SELECT()
  3: 0x02F1 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0320
  4: 0x02F9 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x02FA [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  6: 0x02FC [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  7: 0x02FE [0x03] Work_Zone[1] = 1*
  8: 0x0303 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
  9: 0x030A [0x47] UPDATE_PLAYER_POS(-300.000*, -580.000*, -0.499*, yaw=0.0°*)
 10: 0x0314 [0x47] WAIT_PLAYER_POS_UPDATE
 11: 0x0316 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x05)
 12: 0x031D [0x01] GOTO 0x032B
 13: 0x0320 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x032B
 14: 0x0328 [0x01] GOTO 0x032B

SUBROUTINE_032B:
 15: 0x032B [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 16: 0x032D [0x21] END_EVENT
 17: 0x032E [0x00] END_REQSTACK()
```

### Event 205

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x032F   |
| Data Size    | 72 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0320:                                               20                  
0330: 01 24 0A 80 0B 80 01 80  25 02 00 10 01 80 00 68  .$......%......h
0340: 03 42 43 00 43 01 03 01  10 0B 80 29 01 F0 FF FF  .BC.C......)....
0350: 7F 04 47 00 18 80 19 80  0E 80 01 80 47 01 29 01  ..G.........G.).
0360: F0 FF FF 7F 05 01 73 03  02 00 10 0B 80 00 73 03  ......s.......s.
0370: 01 73 03 20 00 21 00                              .s. .!.         
```

#### Opcodes

```
  0: 0x032F [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0331 [0x24] CREATE_DIALOG(message_id=7440*, default_option=1*, option_flags=0*)
    → "Use the device? [Yes./No.]"
  2: 0x0338 [0x25] WAIT_DIALOG_SELECT()
  3: 0x0339 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0368
  4: 0x0341 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x0342 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  6: 0x0344 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  7: 0x0346 [0x03] Work_Zone[1] = 1*
  8: 0x034B [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
  9: 0x0352 [0x47] UPDATE_PLAYER_POS(-460.000*, -20.000*, -0.499*, yaw=0.0°*)
 10: 0x035C [0x47] WAIT_PLAYER_POS_UPDATE
 11: 0x035E [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x05)
 12: 0x0365 [0x01] GOTO 0x0373
 13: 0x0368 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0373
 14: 0x0370 [0x01] GOTO 0x0373

SUBROUTINE_0373:
 15: 0x0373 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 16: 0x0375 [0x21] END_EVENT
 17: 0x0376 [0x00] END_REQSTACK()
```

### Event 206

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0377   |
| Data Size    | 72 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0370:                      20  01 24 0A 80 0B 80 01 80          .$......
0380: 25 02 00 10 01 80 00 B0  03 42 43 00 43 01 03 01  %........BC.C...
0390: 10 0B 80 29 01 F0 FF FF  7F 04 47 00 1A 80 19 80  ...)......G.....
03A0: 0E 80 12 80 47 01 29 01  F0 FF FF 7F 05 01 BB 03  ....G.).........
03B0: 02 00 10 0B 80 00 BB 03  01 BB 03 20 00 21 00     ........... .!. 
```

#### Opcodes

```
  0: 0x0377 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0379 [0x24] CREATE_DIALOG(message_id=7440*, default_option=1*, option_flags=0*)
    → "Use the device? [Yes./No.]"
  2: 0x0380 [0x25] WAIT_DIALOG_SELECT()
  3: 0x0381 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x03B0
  4: 0x0389 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x038A [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  6: 0x038C [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  7: 0x038E [0x03] Work_Zone[1] = 1*
  8: 0x0393 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
  9: 0x039A [0x47] UPDATE_PLAYER_POS(-220.000*, -20.000*, -0.499*, yaw=180.0°*)
 10: 0x03A4 [0x47] WAIT_PLAYER_POS_UPDATE
 11: 0x03A6 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x05)
 12: 0x03AD [0x01] GOTO 0x03BB
 13: 0x03B0 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x03BB
 14: 0x03B8 [0x01] GOTO 0x03BB

SUBROUTINE_03BB:
 15: 0x03BB [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 16: 0x03BD [0x21] END_EVENT
 17: 0x03BE [0x00] END_REQSTACK()
```

### Event 207

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x03BF   |
| Data Size    | 79 bytes |
| Instructions | 19       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03B0:                                               20                  
03C0: 01 24 0A 80 0B 80 01 80  25 02 00 10 01 80 00 FF  .$......%.......
03D0: 03 42 43 00 43 01 03 01  10 0B 80 29 01 F0 FF FF  .BC.C......)....
03E0: 7F 04 47 00 11 80 0C 80  16 80 0F 80 47 01 29 01  ..G.........G.).
03F0: FC B1 04 01 01 29 01 F0  FF FF 7F 05 01 0A 04 02  .....)..........
0400: 00 10 0B 80 00 0A 04 01  0A 04 20 00 21 00        .......... .!.  
```

#### Opcodes

```
  0: 0x03BF [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x03C1 [0x24] CREATE_DIALOG(message_id=7440*, default_option=1*, option_flags=0*)
    → "Use the device? [Yes./No.]"
  2: 0x03C8 [0x25] WAIT_DIALOG_SELECT()
  3: 0x03C9 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x03FF
  4: 0x03D1 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x03D2 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  6: 0x03D4 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  7: 0x03D6 [0x03] Work_Zone[1] = 1*
  8: 0x03DB [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
  9: 0x03E2 [0x47] UPDATE_PLAYER_POS(-340.000*, 340.000*, -0.500*, yaw=270.0°*)
 10: 0x03EC [0x47] WAIT_PLAYER_POS_UPDATE
 11: 0x03EE [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Weather (ID: 17084924/0x0104B1FC), tag_num=0x01)
 12: 0x03F5 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x05)
 13: 0x03FC [0x01] GOTO 0x040A
 14: 0x03FF [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x040A
 15: 0x0407 [0x01] GOTO 0x040A

SUBROUTINE_040A:
 16: 0x040A [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 17: 0x040C [0x21] END_EVENT
 18: 0x040D [0x00] END_REQSTACK()
```

### Event 208

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x040E   |
| Data Size    | 46 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0400:                                            20 01                 .
0410: 24 0A 80 0B 80 01 80 25  02 00 10 01 80 00 2D 04  $......%......-.
0420: 42 43 00 43 01 03 01 10  0B 80 01 38 04 02 00 10  BC.C.......8....
0430: 0B 80 00 38 04 01 38 04  20 00 21 00              ...8..8. .!.    
```

#### Opcodes

```
  0: 0x040E [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0410 [0x24] CREATE_DIALOG(message_id=7440*, default_option=1*, option_flags=0*)
    → "Use the device? [Yes./No.]"
  2: 0x0417 [0x25] WAIT_DIALOG_SELECT()
  3: 0x0418 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x042D
  4: 0x0420 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x0421 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  6: 0x0423 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  7: 0x0425 [0x03] Work_Zone[1] = 1*
  8: 0x042A [0x01] GOTO 0x0438
  9: 0x042D [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0438
 10: 0x0435 [0x01] GOTO 0x0438

SUBROUTINE_0438:
 11: 0x0438 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 12: 0x043A [0x21] END_EVENT
 13: 0x043B [0x00] END_REQSTACK()
```

### Event 209

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x043C   |
| Data Size    | 79 bytes |
| Instructions | 19       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0430:                                      20 01 24 0A               .$.
0440: 80 0B 80 01 80 25 02 00  10 01 80 00 7C 04 42 43  .....%......|.BC
0450: 00 43 01 03 01 10 0B 80  29 01 F0 FF FF 7F 04 47  .C......)......G
0460: 00 0C 80 0D 80 0E 80 0F  80 47 01 29 01 FC B1 04  .........G.)....
0470: 01 02 29 01 F0 FF FF 7F  05 01 87 04 02 00 10 0B  ..).............
0480: 80 00 87 04 01 87 04 20  00 21 00                 ....... .!.     
```

#### Opcodes

```
  0: 0x043C [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x043E [0x24] CREATE_DIALOG(message_id=7440*, default_option=1*, option_flags=0*)
    → "Use the device? [Yes./No.]"
  2: 0x0445 [0x25] WAIT_DIALOG_SELECT()
  3: 0x0446 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x047C
  4: 0x044E [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x044F [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  6: 0x0451 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  7: 0x0453 [0x03] Work_Zone[1] = 1*
  8: 0x0458 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
  9: 0x045F [0x47] UPDATE_PLAYER_POS(340.000*, 140.000*, -0.499*, yaw=270.0°*)
 10: 0x0469 [0x47] WAIT_PLAYER_POS_UPDATE
 11: 0x046B [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Weather (ID: 17084924/0x0104B1FC), tag_num=0x02)
 12: 0x0472 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x05)
 13: 0x0479 [0x01] GOTO 0x0487
 14: 0x047C [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0487
 15: 0x0484 [0x01] GOTO 0x0487

SUBROUTINE_0487:
 16: 0x0487 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 17: 0x0489 [0x21] END_EVENT
 18: 0x048A [0x00] END_REQSTACK()
```

### Event 300

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x048B   |
| Data Size    | 31 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0480:                                   20 01 24 1B 80              .$..
0490: 0B 80 01 80 25 02 00 10  01 80 00 A6 04 42 03 01  ....%........B..
04A0: 10 0B 80 01 A6 04 20 00  21 00                    ...... .!.      
```

#### Opcodes

```
  0: 0x048B [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x048D [0x24] CREATE_DIALOG(message_id=7442*, default_option=1*, option_flags=0*)
    → "Open the door? [Yes./No.]"
  2: 0x0494 [0x25] WAIT_DIALOG_SELECT()
  3: 0x0495 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x04A6
  4: 0x049D [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x049E [0x03] Work_Zone[1] = 1*
  6: 0x04A3 [0x01] GOTO 0x04A6

SUBROUTINE_04A6:
  7: 0x04A6 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x04A8 [0x21] END_EVENT
  9: 0x04A9 [0x00] END_REQSTACK()
```

### Event 2

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x04AA    |
| Data Size    | 526 bytes |
| Instructions | 86        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
04A0:                                20 01 1C 02 80 41             ....A
04B0: 01 80 1C 80 02 10 02 00  41 1D 80 1E 80 02 10 03  ........A.......
04C0: 00 41 01 80 1C 80 03 10  04 00 41 1D 80 1E 80 03  .A........A.....
04D0: 10 05 00 41 01 80 1C 80  04 10 06 00 41 1D 80 1E  ...A........A...
04E0: 80 04 10 07 00 41 01 80  1C 80 05 10 08 00 41 1D  .....A........A.
04F0: 80 1E 80 05 10 09 00 41  01 80 1C 80 06 10 0A 00  .......A........
0500: 41 1D 80 1E 80 06 10 0B  00 41 01 80 1C 80 07 10  A........A......
0510: 0C 00 41 1D 80 1E 80 07  10 0D 00 41 01 80 1C 80  ..A........A....
0520: 08 10 0E 00 41 1D 80 1E  80 08 10 0F 00 41 01 80  ....A........A..
0530: 1C 80 09 10 10 00 41 1D  80 1E 80 09 10 11 00 03  ......A.........
0540: 03 10 02 00 03 04 10 03  00 03 05 10 04 00 03 06  ................
0550: 10 05 00 03 07 10 06 00  03 08 10 07 00 03 09 10  ................
0560: 08 00 03 00 17 09 00 03  01 17 0A 00 03 02 17 0B  ................
0570: 00 03 03 17 0C 00 03 04  17 0D 00 03 05 17 0E 00  ................
0580: 03 06 17 0F 00 03 07 17  10 00 03 08 17 11 00 03  ................
0590: 00 00 01 80 3C 00 00 01  80 0B 80 02 03 00 01 80  ....<...........
05A0: 02 AA 05 3C 00 00 0B 80  0B 80 02 05 00 01 80 02  ...<............
05B0: B9 05 3C 00 00 1F 80 0B  80 02 07 00 01 80 02 C8  ..<.............
05C0: 05 3C 00 00 20 80 0B 80  02 09 00 01 80 02 D7 05  .<.. ...........
05D0: 3C 00 00 21 80 0B 80 02  0B 00 01 80 02 E6 05 3C  <..!...........<
05E0: 00 00 22 80 0B 80 02 0D  00 01 80 02 F5 05 3C 00  .."...........<.
05F0: 00 23 80 0B 80 02 0F 00  01 80 02 04 06 3C 00 00  .#...........<..
0600: 24 80 0B 80 02 11 00 01  80 02 13 06 3C 00 00 25  $...........<..%
0610: 80 0B 80 03 01 00 26 80  0F 01 00 00 00 24 27 80  ......&......$'.
0620: 01 80 01 00 25 02 00 10  01 80 00 35 06 03 01 10  ....%......5....
0630: 01 80 01 B5 06 02 00 10  0B 80 00 45 06 03 01 10  ...........E....
0640: 0B 80 01 B5 06 02 00 10  1F 80 00 55 06 03 01 10  ...........U....
0650: 1F 80 01 B5 06 02 00 10  20 80 00 65 06 03 01 10  ........ ..e....
0660: 20 80 01 B5 06 02 00 10  21 80 00 75 06 03 01 10   .......!..u....
0670: 21 80 01 B5 06 02 00 10  22 80 00 85 06 03 01 10  !.......".......
0680: 22 80 01 B5 06 02 00 10  23 80 00 95 06 03 01 10  ".......#.......
0690: 23 80 01 B5 06 02 00 10  24 80 00 A5 06 03 01 10  #.......$.......
06A0: 24 80 01 B5 06 02 00 10  25 80 00 B5 06 03 01 10  $.......%.......
06B0: 25 80 01 B5 06 42 21 00                           %....B!.        
```

#### Opcodes

```
  0: 0x04AA [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x04AC [0x1C] WAIT(60* ticks)
  2: 0x04AF [0x41] ExtData[1]->WorkLocal[2] = Work_Zone[2] (bits 0*-15*)
  3: 0x04B8 [0x41] ExtData[1]->WorkLocal[3] = Work_Zone[2] (bits 16*-31*)
  4: 0x04C1 [0x41] ExtData[1]->WorkLocal[4] = Work_Zone[3] (bits 0*-15*)
  5: 0x04CA [0x41] ExtData[1]->WorkLocal[5] = Work_Zone[3] (bits 16*-31*)
  6: 0x04D3 [0x41] ExtData[1]->WorkLocal[6] = Work_Zone[4] (bits 0*-15*)
  7: 0x04DC [0x41] ExtData[1]->WorkLocal[7] = Work_Zone[4] (bits 16*-31*)
  8: 0x04E5 [0x41] ExtData[1]->WorkLocal[8] = Work_Zone[5] (bits 0*-15*)
  9: 0x04EE [0x41] ExtData[1]->WorkLocal[9] = Work_Zone[5] (bits 16*-31*)
 10: 0x04F7 [0x41] ExtData[1]->WorkLocal[10] = Work_Zone[6] (bits 0*-15*)
 11: 0x0500 [0x41] ExtData[1]->WorkLocal[11] = Work_Zone[6] (bits 16*-31*)
 12: 0x0509 [0x41] ExtData[1]->WorkLocal[12] = Work_Zone[7] (bits 0*-15*)
 13: 0x0512 [0x41] ExtData[1]->WorkLocal[13] = Work_Zone[7] (bits 16*-31*)
 14: 0x051B [0x41] ExtData[1]->WorkLocal[14] = Work_Zone[8] (bits 0*-15*)
 15: 0x0524 [0x41] ExtData[1]->WorkLocal[15] = Work_Zone[8] (bits 16*-31*)
 16: 0x052D [0x41] ExtData[1]->WorkLocal[16] = Work_Zone[9] (bits 0*-15*)
 17: 0x0536 [0x41] ExtData[1]->WorkLocal[17] = Work_Zone[9] (bits 16*-31*)
 18: 0x053F [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[2]
 19: 0x0544 [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[3]
 20: 0x0549 [0x03] Work_Zone[5] = ExtData[1]->WorkLocal[4]
 21: 0x054E [0x03] Work_Zone[6] = ExtData[1]->WorkLocal[5]
 22: 0x0553 [0x03] Work_Zone[7] = ExtData[1]->WorkLocal[6]
 23: 0x0558 [0x03] Work_Zone[8] = ExtData[1]->WorkLocal[7]
 24: 0x055D [0x03] Work_Zone[9] = ExtData[1]->WorkLocal[8]
 25: 0x0562 [0x03] Work_Zone_1700[0] = ExtData[1]->WorkLocal[9]
 26: 0x0567 [0x03] Work_Zone_1700[1] = ExtData[1]->WorkLocal[10]
 27: 0x056C [0x03] Work_Zone_1700[2] = ExtData[1]->WorkLocal[11]
 28: 0x0571 [0x03] Work_Zone_1700[3] = ExtData[1]->WorkLocal[12]
 29: 0x0576 [0x03] Work_Zone_1700[4] = ExtData[1]->WorkLocal[13]
 30: 0x057B [0x03] Work_Zone_1700[5] = ExtData[1]->WorkLocal[14]
 31: 0x0580 [0x03] Work_Zone_1700[6] = ExtData[1]->WorkLocal[15]
 32: 0x0585 [0x03] Work_Zone_1700[7] = ExtData[1]->WorkLocal[16]
 33: 0x058A [0x03] Work_Zone_1700[8] = ExtData[1]->WorkLocal[17]
 34: 0x058F [0x03] ExtData[1]->WorkLocal[0] = 0*
 35: 0x0594 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=0*, condition_work_offset=1*)
 36: 0x059B [0x02] IF !(ExtData[1]->WorkLocal[3] <= 0*) GOTO 0x05AA
 37: 0x05A3 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=1*, condition_work_offset=1*)
 38: 0x05AA [0x02] IF !(ExtData[1]->WorkLocal[5] <= 0*) GOTO 0x05B9
 39: 0x05B2 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=2*, condition_work_offset=1*)
 40: 0x05B9 [0x02] IF !(ExtData[1]->WorkLocal[7] <= 0*) GOTO 0x05C8
 41: 0x05C1 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=3*, condition_work_offset=1*)
 42: 0x05C8 [0x02] IF !(ExtData[1]->WorkLocal[9] <= 0*) GOTO 0x05D7
 43: 0x05D0 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=4*, condition_work_offset=1*)
 44: 0x05D7 [0x02] IF !(ExtData[1]->WorkLocal[11] <= 0*) GOTO 0x05E6
 45: 0x05DF [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=5*, condition_work_offset=1*)
 46: 0x05E6 [0x02] IF !(ExtData[1]->WorkLocal[13] <= 0*) GOTO 0x05F5
 47: 0x05EE [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=6*, condition_work_offset=1*)
 48: 0x05F5 [0x02] IF !(ExtData[1]->WorkLocal[15] <= 0*) GOTO 0x0604
 49: 0x05FD [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=7*, condition_work_offset=1*)
 50: 0x0604 [0x02] IF !(ExtData[1]->WorkLocal[17] <= 0*) GOTO 0x0613
 51: 0x060C [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=8*, condition_work_offset=1*)
 52: 0x0613 [0x03] ExtData[1]->WorkLocal[1] = 4294967295*
 53: 0x0618 [0x0F] ExtData[1]->WorkLocal[1] ^= ExtData[1]->WorkLocal[0]
 54: 0x061D [0x24] CREATE_DIALOG(message_id=7247*, default_option=0*, option_flags=ExtData[1]->WorkLocal[1])
    → "What do you take? [Nothing./$1 ($2 remaining)/$3 ($4 remaining)/$5 ($6 remaining)/$7 ($8 remaining)/$9 ($10 remaining)/$11 ($12 remaining)/$13 ($14 remaining)/$15 ($16 remaining)]"
 55: 0x0624 [0x25] WAIT_DIALOG_SELECT()
 56: 0x0625 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0635
 57: 0x062D [0x03] Work_Zone[1] = 0*
 58: 0x0632 [0x01] GOTO 0x06B5
 59: 0x0635 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0645
 60: 0x063D [0x03] Work_Zone[1] = 1*
 61: 0x0642 [0x01] GOTO 0x06B5
 62: 0x0645 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0655
 63: 0x064D [0x03] Work_Zone[1] = 2*
 64: 0x0652 [0x01] GOTO 0x06B5
 65: 0x0655 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0665
 66: 0x065D [0x03] Work_Zone[1] = 3*
 67: 0x0662 [0x01] GOTO 0x06B5
 68: 0x0665 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x0675
 69: 0x066D [0x03] Work_Zone[1] = 4*
 70: 0x0672 [0x01] GOTO 0x06B5
 71: 0x0675 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x0685
 72: 0x067D [0x03] Work_Zone[1] = 5*
 73: 0x0682 [0x01] GOTO 0x06B5
 74: 0x0685 [0x02] IF !(Work_Zone[0] == 6*) GOTO 0x0695
 75: 0x068D [0x03] Work_Zone[1] = 6*
 76: 0x0692 [0x01] GOTO 0x06B5
 77: 0x0695 [0x02] IF !(Work_Zone[0] == 7*) GOTO 0x06A5
 78: 0x069D [0x03] Work_Zone[1] = 7*
 79: 0x06A2 [0x01] GOTO 0x06B5
 80: 0x06A5 [0x02] IF !(Work_Zone[0] == 8*) GOTO 0x06B5
 81: 0x06AD [0x03] Work_Zone[1] = 8*
 82: 0x06B2 [0x01] GOTO 0x06B5

SUBROUTINE_06B5:
 83: 0x06B5 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 84: 0x06B6 [0x21] END_EVENT
 85: 0x06B7 [0x00] END_REQSTACK()
```

### Event 3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x06B8   |
| Data Size    | 35 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
06B0:                          20 01 24 28 80 0B 80 01           .$(....
06C0: 80 25 02 00 10 01 80 00  D7 06 43 00 43 01 42 03  .%........C.C.B.
06D0: 01 10 0B 80 01 D7 06 20  00 21 00                 ....... .!.     
```

#### Opcodes

```
  0: 0x06B8 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x06BA [0x24] CREATE_DIALOG(message_id=7444*, default_option=1*, option_flags=0*)
    → "Open the gate? [Yes./No.]"
  2: 0x06C1 [0x25] WAIT_DIALOG_SELECT()
  3: 0x06C2 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x06D7
  4: 0x06CA [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  5: 0x06CC [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  6: 0x06CE [0x42] SET_CLI_EVENT_CANCEL_DATA()
  7: 0x06CF [0x03] Work_Zone[1] = 1*
  8: 0x06D4 [0x01] GOTO 0x06D7

SUBROUTINE_06D7:
  9: 0x06D7 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x06D9 [0x21] END_EVENT
 11: 0x06DA [0x00] END_REQSTACK()
```
