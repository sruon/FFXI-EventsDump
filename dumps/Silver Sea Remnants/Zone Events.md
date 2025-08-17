# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Silver Sea Remnants (ID: 76) |
| Block Size       | 1900 bytes                   |
| Total Events     | 21                           |
| References Count | 41                           |

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
| [3](#event-3)         | 0x0107       |    108 |             16 |
| [200](#event-200)     | 0x0173       |     72 |             18 |
| [201](#event-201)     | 0x01BB       |     72 |             18 |
| [202](#event-202)     | 0x0203       |     72 |             18 |
| [203](#event-203)     | 0x024B       |     72 |             18 |
| [204](#event-204)     | 0x0293       |     72 |             18 |
| [205](#event-205)     | 0x02DB       |     72 |             18 |
| [206](#event-206)     | 0x0323       |     72 |             18 |
| [207](#event-207)     | 0x036B       |     79 |             19 |
| [208](#event-208)     | 0x03BA       |     46 |             14 |
| [209](#event-209)     | 0x03E8       |     79 |             19 |
| [300](#event-300)     | 0x0437       |     31 |             10 |
| [2](#event-2)         | 0x0456       |    526 |             86 |

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
|      13 | 0x83D60     |      540000 |
|      14 | 0xFFFFFE0D  |  4294966797 |
|      15 | 0x0400      |        1024 |
|      16 | 0xFFF99760  |  4294547296 |
|      17 | 0xFFF8FB20  |  4294507296 |
|      18 | 0xFFFFFE0C  |  4294966796 |
|      19 | 0x0800      |        2048 |
|      20 | 0xFFFA33A0  |  4294587296 |
|      21 | 0xFFFCA4A0  |  4294747296 |
|      22 | 0xFFFC0860  |  4294707296 |
|      23 | 0x1000      |        4096 |
|      24 | 0xFFFB6C20  |  4294667296 |
|      25 | 0x2BF20     |      180000 |
|      26 | 0xFFFACFE0  |  4294627296 |
|      27 | 0xA1220     |      660000 |
|      28 | 0x1D12      |        7442 |
|      29 | 0x000F      |          15 |
|      30 | 0x0010      |          16 |
|      31 | 0x001F      |          31 |
|      32 | 0x0002      |           2 |
|      33 | 0x0003      |           3 |
|      34 | 0x0004      |           4 |
|      35 | 0x0005      |           5 |
|      36 | 0x0006      |           6 |
|      37 | 0x0007      |           7 |
|      38 | 0x0008      |           8 |
|      39 | 0xFFFFFFFF  |  4294967295 |
|      40 | 0x1C4F      |        7247 |

## String References

- **7247**: What do you take? [Nothing./$1 ($2 remaining)/$3 ($4 remaining)/$5 ($6 remaining)/$7 ($8 remaining)/$9 ($10 remaining)/$11 ($12 remaining)/$13 ($14 remaining)/$15 ($16 remaining)]
- **7440**: Use the device? [Yes./No.]
- **7442**: Open the door? [Yes./No.]

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
00B0: 80 1C 02 80 29 01 8C C3  04 01 01 45 00 80 F0 FF  ....)......E....
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
  6: 0x00B4 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Weather (ID: 17089420/0x0104C38C), tag_num=0x01)
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
00E0: FF 7F 66 64 6F 31 01 80  1C 02 80 29 01 8C C3 04  ..fdo1.....)....
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
  6: 0x00EB [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Weather (ID: 17089420/0x0104C38C), tag_num=0x02)
  7: 0x00F2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  8: 0x0103 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  9: 0x0105 [0x21] END_EVENT
 10: 0x0106 [0x00] END_REQSTACK()
```

### Event 3

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
0130: 3E 02 10 08 80 41 01 29  01 8C C3 04 01 01 01 48  >....A.).......H
0140: 01 29 01 8C C3 04 01 02  43 00 43 01 45 00 80 F0  .)......C.C.E...
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
  6: 0x0137 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Weather (ID: 17089420/0x0104C38C), tag_num=0x01)
  7: 0x013E [0x01] GOTO 0x0148
  8: 0x0141 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Weather (ID: 17089420/0x0104C38C), tag_num=0x02)

SUBROUTINE_0148:
  9: 0x0148 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 10: 0x014A [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 11: 0x014C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 12: 0x015D [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [EventEntity, EventEntity], work=[231*, 0*]
 13: 0x016E [0x1C] WAIT(120* ticks)
 14: 0x0171 [0x21] END_EVENT
 15: 0x0172 [0x00] END_REQSTACK()
```

### Event 200

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0173   |
| Data Size    | 72 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:          20 01 24 0A 80  0B 80 01 80 25 02 00 10      .$......%...
0180: 01 80 00 AC 01 42 43 00  43 01 03 01 10 0B 80 29  .....BC.C......)
0190: 01 F0 FF FF 7F 04 47 00  0C 80 0D 80 0E 80 0F 80  ......G.........
01A0: 47 01 29 01 F0 FF FF 7F  05 01 B7 01 02 00 10 0B  G.).............
01B0: 80 00 B7 01 01 B7 01 20  00 21 00                 ....... .!.     
```

#### Opcodes

```
  0: 0x0173 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0175 [0x24] CREATE_DIALOG(message_id=7440*, default_option=1*, option_flags=0*)
    → "Use the device? [Yes./No.]"
  2: 0x017C [0x25] WAIT_DIALOG_SELECT()
  3: 0x017D [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01AC
  4: 0x0185 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x0186 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  6: 0x0188 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  7: 0x018A [0x03] Work_Zone[1] = 1*
  8: 0x018F [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
  9: 0x0196 [0x47] UPDATE_PLAYER_POS(340.000*, 540.000*, -0.499*, yaw=90.0°*)
 10: 0x01A0 [0x47] WAIT_PLAYER_POS_UPDATE
 11: 0x01A2 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x05)
 12: 0x01A9 [0x01] GOTO 0x01B7
 13: 0x01AC [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x01B7
 14: 0x01B4 [0x01] GOTO 0x01B7

SUBROUTINE_01B7:
 15: 0x01B7 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 16: 0x01B9 [0x21] END_EVENT
 17: 0x01BA [0x00] END_REQSTACK()
```

### Event 201

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01BB   |
| Data Size    | 72 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:                                   20 01 24 0A 80              .$..
01C0: 0B 80 01 80 25 02 00 10  01 80 00 F4 01 42 43 00  ....%........BC.
01D0: 43 01 03 01 10 0B 80 29  01 F0 FF FF 7F 04 47 00  C......)......G.
01E0: 10 80 11 80 12 80 13 80  47 01 29 01 F0 FF FF 7F  ........G.).....
01F0: 05 01 FF 01 02 00 10 0B  80 00 FF 01 01 FF 01 20  ............... 
0200: 00 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x01BB [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x01BD [0x24] CREATE_DIALOG(message_id=7440*, default_option=1*, option_flags=0*)
    → "Use the device? [Yes./No.]"
  2: 0x01C4 [0x25] WAIT_DIALOG_SELECT()
  3: 0x01C5 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01F4
  4: 0x01CD [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x01CE [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  6: 0x01D0 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  7: 0x01D2 [0x03] Work_Zone[1] = 1*
  8: 0x01D7 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
  9: 0x01DE [0x47] UPDATE_PLAYER_POS(-420.000*, -460.000*, -0.500*, yaw=180.0°*)
 10: 0x01E8 [0x47] WAIT_PLAYER_POS_UPDATE
 11: 0x01EA [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x05)
 12: 0x01F1 [0x01] GOTO 0x01FF
 13: 0x01F4 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x01FF
 14: 0x01FC [0x01] GOTO 0x01FF

SUBROUTINE_01FF:
 15: 0x01FF [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 16: 0x0201 [0x21] END_EVENT
 17: 0x0202 [0x00] END_REQSTACK()
```

### Event 202

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0203   |
| Data Size    | 72 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0200:          20 01 24 0A 80  0B 80 01 80 25 02 00 10      .$......%...
0210: 01 80 00 3C 02 42 43 00  43 01 03 01 10 0B 80 29  ...<.BC.C......)
0220: 01 F0 FF FF 7F 04 47 00  14 80 15 80 0E 80 13 80  ......G.........
0230: 47 01 29 01 F0 FF FF 7F  05 01 47 02 02 00 10 0B  G.).......G.....
0240: 80 00 47 02 01 47 02 20  00 21 00                 ..G..G. .!.     
```

#### Opcodes

```
  0: 0x0203 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0205 [0x24] CREATE_DIALOG(message_id=7440*, default_option=1*, option_flags=0*)
    → "Use the device? [Yes./No.]"
  2: 0x020C [0x25] WAIT_DIALOG_SELECT()
  3: 0x020D [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x023C
  4: 0x0215 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x0216 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  6: 0x0218 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  7: 0x021A [0x03] Work_Zone[1] = 1*
  8: 0x021F [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
  9: 0x0226 [0x47] UPDATE_PLAYER_POS(-380.000*, -220.000*, -0.499*, yaw=180.0°*)
 10: 0x0230 [0x47] WAIT_PLAYER_POS_UPDATE
 11: 0x0232 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x05)
 12: 0x0239 [0x01] GOTO 0x0247
 13: 0x023C [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0247
 14: 0x0244 [0x01] GOTO 0x0247

SUBROUTINE_0247:
 15: 0x0247 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 16: 0x0249 [0x21] END_EVENT
 17: 0x024A [0x00] END_REQSTACK()
```

### Event 203

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x024B   |
| Data Size    | 72 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0240:                                   20 01 24 0A 80              .$..
0250: 0B 80 01 80 25 02 00 10  01 80 00 84 02 42 43 00  ....%........BC.
0260: 43 01 03 01 10 0B 80 29  01 F0 FF FF 7F 04 47 00  C......)......G.
0270: 16 80 11 80 12 80 17 80  47 01 29 01 F0 FF FF 7F  ........G.).....
0280: 05 01 8F 02 02 00 10 0B  80 00 8F 02 01 8F 02 20  ............... 
0290: 00 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x024B [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x024D [0x24] CREATE_DIALOG(message_id=7440*, default_option=1*, option_flags=0*)
    → "Use the device? [Yes./No.]"
  2: 0x0254 [0x25] WAIT_DIALOG_SELECT()
  3: 0x0255 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0284
  4: 0x025D [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x025E [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  6: 0x0260 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  7: 0x0262 [0x03] Work_Zone[1] = 1*
  8: 0x0267 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
  9: 0x026E [0x47] UPDATE_PLAYER_POS(-260.000*, -460.000*, -0.500*, yaw=360.0°*)
 10: 0x0278 [0x47] WAIT_PLAYER_POS_UPDATE
 11: 0x027A [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x05)
 12: 0x0281 [0x01] GOTO 0x028F
 13: 0x0284 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x028F
 14: 0x028C [0x01] GOTO 0x028F

SUBROUTINE_028F:
 15: 0x028F [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 16: 0x0291 [0x21] END_EVENT
 17: 0x0292 [0x00] END_REQSTACK()
```

### Event 204

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0293   |
| Data Size    | 72 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0290:          20 01 24 0A 80  0B 80 01 80 25 02 00 10      .$......%...
02A0: 01 80 00 CC 02 42 43 00  43 01 03 01 10 0B 80 29  .....BC.C......)
02B0: 01 F0 FF FF 7F 04 47 00  18 80 15 80 12 80 17 80  ......G.........
02C0: 47 01 29 01 F0 FF FF 7F  05 01 D7 02 02 00 10 0B  G.).............
02D0: 80 00 D7 02 01 D7 02 20  00 21 00                 ....... .!.     
```

#### Opcodes

```
  0: 0x0293 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0295 [0x24] CREATE_DIALOG(message_id=7440*, default_option=1*, option_flags=0*)
    → "Use the device? [Yes./No.]"
  2: 0x029C [0x25] WAIT_DIALOG_SELECT()
  3: 0x029D [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x02CC
  4: 0x02A5 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x02A6 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  6: 0x02A8 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  7: 0x02AA [0x03] Work_Zone[1] = 1*
  8: 0x02AF [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
  9: 0x02B6 [0x47] UPDATE_PLAYER_POS(-300.000*, -220.000*, -0.500*, yaw=360.0°*)
 10: 0x02C0 [0x47] WAIT_PLAYER_POS_UPDATE
 11: 0x02C2 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x05)
 12: 0x02C9 [0x01] GOTO 0x02D7
 13: 0x02CC [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x02D7
 14: 0x02D4 [0x01] GOTO 0x02D7

SUBROUTINE_02D7:
 15: 0x02D7 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 16: 0x02D9 [0x21] END_EVENT
 17: 0x02DA [0x00] END_REQSTACK()
```

### Event 205

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x02DB   |
| Data Size    | 72 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02D0:                                   20 01 24 0A 80              .$..
02E0: 0B 80 01 80 25 02 00 10  01 80 00 14 03 42 43 00  ....%........BC.
02F0: 43 01 03 01 10 0B 80 29  01 F0 FF FF 7F 04 47 00  C......)......G.
0300: 11 80 19 80 0E 80 17 80  47 01 29 01 F0 FF FF 7F  ........G.).....
0310: 05 01 1F 03 02 00 10 0B  80 00 1F 03 01 1F 03 20  ............... 
0320: 00 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x02DB [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x02DD [0x24] CREATE_DIALOG(message_id=7440*, default_option=1*, option_flags=0*)
    → "Use the device? [Yes./No.]"
  2: 0x02E4 [0x25] WAIT_DIALOG_SELECT()
  3: 0x02E5 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0314
  4: 0x02ED [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x02EE [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  6: 0x02F0 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  7: 0x02F2 [0x03] Work_Zone[1] = 1*
  8: 0x02F7 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
  9: 0x02FE [0x47] UPDATE_PLAYER_POS(-460.000*, 180.000*, -0.499*, yaw=360.0°*)
 10: 0x0308 [0x47] WAIT_PLAYER_POS_UPDATE
 11: 0x030A [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x05)
 12: 0x0311 [0x01] GOTO 0x031F
 13: 0x0314 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x031F
 14: 0x031C [0x01] GOTO 0x031F

SUBROUTINE_031F:
 15: 0x031F [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 16: 0x0321 [0x21] END_EVENT
 17: 0x0322 [0x00] END_REQSTACK()
```

### Event 206

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0323   |
| Data Size    | 72 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0320:          20 01 24 0A 80  0B 80 01 80 25 02 00 10      .$......%...
0330: 01 80 00 5C 03 42 43 00  43 01 03 01 10 0B 80 29  ...\.BC.C......)
0340: 01 F0 FF FF 7F 04 47 00  15 80 19 80 12 80 13 80  ......G.........
0350: 47 01 29 01 F0 FF FF 7F  05 01 67 03 02 00 10 0B  G.).......g.....
0360: 80 00 67 03 01 67 03 20  00 21 00                 ..g..g. .!.     
```

#### Opcodes

```
  0: 0x0323 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0325 [0x24] CREATE_DIALOG(message_id=7440*, default_option=1*, option_flags=0*)
    → "Use the device? [Yes./No.]"
  2: 0x032C [0x25] WAIT_DIALOG_SELECT()
  3: 0x032D [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x035C
  4: 0x0335 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x0336 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  6: 0x0338 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  7: 0x033A [0x03] Work_Zone[1] = 1*
  8: 0x033F [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
  9: 0x0346 [0x47] UPDATE_PLAYER_POS(-220.000*, 180.000*, -0.500*, yaw=180.0°*)
 10: 0x0350 [0x47] WAIT_PLAYER_POS_UPDATE
 11: 0x0352 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x05)
 12: 0x0359 [0x01] GOTO 0x0367
 13: 0x035C [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0367
 14: 0x0364 [0x01] GOTO 0x0367

SUBROUTINE_0367:
 15: 0x0367 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 16: 0x0369 [0x21] END_EVENT
 17: 0x036A [0x00] END_REQSTACK()
```

### Event 207

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x036B   |
| Data Size    | 79 bytes |
| Instructions | 19       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0360:                                   20 01 24 0A 80              .$..
0370: 0B 80 01 80 25 02 00 10  01 80 00 AB 03 42 43 00  ....%........BC.
0380: 43 01 03 01 10 0B 80 29  01 F0 FF FF 7F 04 47 00  C......)......G.
0390: 1A 80 1B 80 12 80 0F 80  47 01 29 01 8C C3 04 01  ........G.).....
03A0: 01 29 01 F0 FF FF 7F 05  01 B6 03 02 00 10 0B 80  .)..............
03B0: 00 B6 03 01 B6 03 20 00  21 00                    ...... .!.      
```

#### Opcodes

```
  0: 0x036B [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x036D [0x24] CREATE_DIALOG(message_id=7440*, default_option=1*, option_flags=0*)
    → "Use the device? [Yes./No.]"
  2: 0x0374 [0x25] WAIT_DIALOG_SELECT()
  3: 0x0375 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x03AB
  4: 0x037D [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x037E [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  6: 0x0380 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  7: 0x0382 [0x03] Work_Zone[1] = 1*
  8: 0x0387 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
  9: 0x038E [0x47] UPDATE_PLAYER_POS(-340.000*, 660.000*, -0.500*, yaw=90.0°*)
 10: 0x0398 [0x47] WAIT_PLAYER_POS_UPDATE
 11: 0x039A [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Weather (ID: 17089420/0x0104C38C), tag_num=0x01)
 12: 0x03A1 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x05)
 13: 0x03A8 [0x01] GOTO 0x03B6
 14: 0x03AB [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x03B6
 15: 0x03B3 [0x01] GOTO 0x03B6

SUBROUTINE_03B6:
 16: 0x03B6 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 17: 0x03B8 [0x21] END_EVENT
 18: 0x03B9 [0x00] END_REQSTACK()
```

### Event 208

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x03BA   |
| Data Size    | 46 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03B0:                                20 01 24 0A 80 0B             .$...
03C0: 80 01 80 25 02 00 10 01  80 00 D9 03 42 43 00 43  ...%........BC.C
03D0: 01 03 01 10 0B 80 01 E4  03 02 00 10 0B 80 00 E4  ................
03E0: 03 01 E4 03 20 00 21 00                           .... .!.        
```

#### Opcodes

```
  0: 0x03BA [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x03BC [0x24] CREATE_DIALOG(message_id=7440*, default_option=1*, option_flags=0*)
    → "Use the device? [Yes./No.]"
  2: 0x03C3 [0x25] WAIT_DIALOG_SELECT()
  3: 0x03C4 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x03D9
  4: 0x03CC [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x03CD [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  6: 0x03CF [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  7: 0x03D1 [0x03] Work_Zone[1] = 1*
  8: 0x03D6 [0x01] GOTO 0x03E4
  9: 0x03D9 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x03E4
 10: 0x03E1 [0x01] GOTO 0x03E4

SUBROUTINE_03E4:
 11: 0x03E4 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 12: 0x03E6 [0x21] END_EVENT
 13: 0x03E7 [0x00] END_REQSTACK()
```

### Event 209

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x03E8   |
| Data Size    | 79 bytes |
| Instructions | 19       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03E0:                          20 01 24 0A 80 0B 80 01           .$.....
03F0: 80 25 02 00 10 01 80 00  28 04 42 43 00 43 01 03  .%......(.BC.C..
0400: 01 10 0B 80 29 01 F0 FF  FF 7F 04 47 00 0C 80 0D  ....)......G....
0410: 80 0E 80 0F 80 47 01 29  01 8C C3 04 01 02 29 01  .....G.)......).
0420: F0 FF FF 7F 05 01 33 04  02 00 10 0B 80 00 33 04  ......3.......3.
0430: 01 33 04 20 00 21 00                              .3. .!.         
```

#### Opcodes

```
  0: 0x03E8 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x03EA [0x24] CREATE_DIALOG(message_id=7440*, default_option=1*, option_flags=0*)
    → "Use the device? [Yes./No.]"
  2: 0x03F1 [0x25] WAIT_DIALOG_SELECT()
  3: 0x03F2 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0428
  4: 0x03FA [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x03FB [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  6: 0x03FD [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  7: 0x03FF [0x03] Work_Zone[1] = 1*
  8: 0x0404 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
  9: 0x040B [0x47] UPDATE_PLAYER_POS(340.000*, 540.000*, -0.499*, yaw=90.0°*)
 10: 0x0415 [0x47] WAIT_PLAYER_POS_UPDATE
 11: 0x0417 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Weather (ID: 17089420/0x0104C38C), tag_num=0x02)
 12: 0x041E [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x05)
 13: 0x0425 [0x01] GOTO 0x0433
 14: 0x0428 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0433
 15: 0x0430 [0x01] GOTO 0x0433

SUBROUTINE_0433:
 16: 0x0433 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 17: 0x0435 [0x21] END_EVENT
 18: 0x0436 [0x00] END_REQSTACK()
```

### Event 300

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0437   |
| Data Size    | 31 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0430:                      20  01 24 1C 80 0B 80 01 80          .$......
0440: 25 02 00 10 01 80 00 52  04 42 03 01 10 0B 80 01  %......R.B......
0450: 52 04 20 00 21 00                                 R. .!.          
```

#### Opcodes

```
  0: 0x0437 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0439 [0x24] CREATE_DIALOG(message_id=7442*, default_option=1*, option_flags=0*)
    → "Open the door? [Yes./No.]"
  2: 0x0440 [0x25] WAIT_DIALOG_SELECT()
  3: 0x0441 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0452
  4: 0x0449 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x044A [0x03] Work_Zone[1] = 1*
  6: 0x044F [0x01] GOTO 0x0452

SUBROUTINE_0452:
  7: 0x0452 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x0454 [0x21] END_EVENT
  9: 0x0455 [0x00] END_REQSTACK()
```

### Event 2

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0456    |
| Data Size    | 526 bytes |
| Instructions | 86        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0450:                   20 01  1C 02 80 41 01 80 1D 80         ....A....
0460: 02 10 02 00 41 1E 80 1F  80 02 10 03 00 41 01 80  ....A........A..
0470: 1D 80 03 10 04 00 41 1E  80 1F 80 03 10 05 00 41  ......A........A
0480: 01 80 1D 80 04 10 06 00  41 1E 80 1F 80 04 10 07  ........A.......
0490: 00 41 01 80 1D 80 05 10  08 00 41 1E 80 1F 80 05  .A........A.....
04A0: 10 09 00 41 01 80 1D 80  06 10 0A 00 41 1E 80 1F  ...A........A...
04B0: 80 06 10 0B 00 41 01 80  1D 80 07 10 0C 00 41 1E  .....A........A.
04C0: 80 1F 80 07 10 0D 00 41  01 80 1D 80 08 10 0E 00  .......A........
04D0: 41 1E 80 1F 80 08 10 0F  00 41 01 80 1D 80 09 10  A........A......
04E0: 10 00 41 1E 80 1F 80 09  10 11 00 03 03 10 02 00  ..A.............
04F0: 03 04 10 03 00 03 05 10  04 00 03 06 10 05 00 03  ................
0500: 07 10 06 00 03 08 10 07  00 03 09 10 08 00 03 00  ................
0510: 17 09 00 03 01 17 0A 00  03 02 17 0B 00 03 03 17  ................
0520: 0C 00 03 04 17 0D 00 03  05 17 0E 00 03 06 17 0F  ................
0530: 00 03 07 17 10 00 03 08  17 11 00 03 00 00 01 80  ................
0540: 3C 00 00 01 80 0B 80 02  03 00 01 80 02 56 05 3C  <............V.<
0550: 00 00 0B 80 0B 80 02 05  00 01 80 02 65 05 3C 00  ............e.<.
0560: 00 20 80 0B 80 02 07 00  01 80 02 74 05 3C 00 00  . .........t.<..
0570: 21 80 0B 80 02 09 00 01  80 02 83 05 3C 00 00 22  !...........<.."
0580: 80 0B 80 02 0B 00 01 80  02 92 05 3C 00 00 23 80  ...........<..#.
0590: 0B 80 02 0D 00 01 80 02  A1 05 3C 00 00 24 80 0B  ..........<..$..
05A0: 80 02 0F 00 01 80 02 B0  05 3C 00 00 25 80 0B 80  .........<..%...
05B0: 02 11 00 01 80 02 BF 05  3C 00 00 26 80 0B 80 03  ........<..&....
05C0: 01 00 27 80 0F 01 00 00  00 24 28 80 01 80 01 00  ..'......$(.....
05D0: 25 02 00 10 01 80 00 E1  05 03 01 10 01 80 01 61  %..............a
05E0: 06 02 00 10 0B 80 00 F1  05 03 01 10 0B 80 01 61  ...............a
05F0: 06 02 00 10 20 80 00 01  06 03 01 10 20 80 01 61  .... ....... ..a
0600: 06 02 00 10 21 80 00 11  06 03 01 10 21 80 01 61  ....!.......!..a
0610: 06 02 00 10 22 80 00 21  06 03 01 10 22 80 01 61  ...."..!...."..a
0620: 06 02 00 10 23 80 00 31  06 03 01 10 23 80 01 61  ....#..1....#..a
0630: 06 02 00 10 24 80 00 41  06 03 01 10 24 80 01 61  ....$..A....$..a
0640: 06 02 00 10 25 80 00 51  06 03 01 10 25 80 01 61  ....%..Q....%..a
0650: 06 02 00 10 26 80 00 61  06 03 01 10 26 80 01 61  ....&..a....&..a
0660: 06 42 21 00                                       .B!.            
```

#### Opcodes

```
  0: 0x0456 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0458 [0x1C] WAIT(60* ticks)
  2: 0x045B [0x41] ExtData[1]->WorkLocal[2] = Work_Zone[2] (bits 0*-15*)
  3: 0x0464 [0x41] ExtData[1]->WorkLocal[3] = Work_Zone[2] (bits 16*-31*)
  4: 0x046D [0x41] ExtData[1]->WorkLocal[4] = Work_Zone[3] (bits 0*-15*)
  5: 0x0476 [0x41] ExtData[1]->WorkLocal[5] = Work_Zone[3] (bits 16*-31*)
  6: 0x047F [0x41] ExtData[1]->WorkLocal[6] = Work_Zone[4] (bits 0*-15*)
  7: 0x0488 [0x41] ExtData[1]->WorkLocal[7] = Work_Zone[4] (bits 16*-31*)
  8: 0x0491 [0x41] ExtData[1]->WorkLocal[8] = Work_Zone[5] (bits 0*-15*)
  9: 0x049A [0x41] ExtData[1]->WorkLocal[9] = Work_Zone[5] (bits 16*-31*)
 10: 0x04A3 [0x41] ExtData[1]->WorkLocal[10] = Work_Zone[6] (bits 0*-15*)
 11: 0x04AC [0x41] ExtData[1]->WorkLocal[11] = Work_Zone[6] (bits 16*-31*)
 12: 0x04B5 [0x41] ExtData[1]->WorkLocal[12] = Work_Zone[7] (bits 0*-15*)
 13: 0x04BE [0x41] ExtData[1]->WorkLocal[13] = Work_Zone[7] (bits 16*-31*)
 14: 0x04C7 [0x41] ExtData[1]->WorkLocal[14] = Work_Zone[8] (bits 0*-15*)
 15: 0x04D0 [0x41] ExtData[1]->WorkLocal[15] = Work_Zone[8] (bits 16*-31*)
 16: 0x04D9 [0x41] ExtData[1]->WorkLocal[16] = Work_Zone[9] (bits 0*-15*)
 17: 0x04E2 [0x41] ExtData[1]->WorkLocal[17] = Work_Zone[9] (bits 16*-31*)
 18: 0x04EB [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[2]
 19: 0x04F0 [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[3]
 20: 0x04F5 [0x03] Work_Zone[5] = ExtData[1]->WorkLocal[4]
 21: 0x04FA [0x03] Work_Zone[6] = ExtData[1]->WorkLocal[5]
 22: 0x04FF [0x03] Work_Zone[7] = ExtData[1]->WorkLocal[6]
 23: 0x0504 [0x03] Work_Zone[8] = ExtData[1]->WorkLocal[7]
 24: 0x0509 [0x03] Work_Zone[9] = ExtData[1]->WorkLocal[8]
 25: 0x050E [0x03] Work_Zone_1700[0] = ExtData[1]->WorkLocal[9]
 26: 0x0513 [0x03] Work_Zone_1700[1] = ExtData[1]->WorkLocal[10]
 27: 0x0518 [0x03] Work_Zone_1700[2] = ExtData[1]->WorkLocal[11]
 28: 0x051D [0x03] Work_Zone_1700[3] = ExtData[1]->WorkLocal[12]
 29: 0x0522 [0x03] Work_Zone_1700[4] = ExtData[1]->WorkLocal[13]
 30: 0x0527 [0x03] Work_Zone_1700[5] = ExtData[1]->WorkLocal[14]
 31: 0x052C [0x03] Work_Zone_1700[6] = ExtData[1]->WorkLocal[15]
 32: 0x0531 [0x03] Work_Zone_1700[7] = ExtData[1]->WorkLocal[16]
 33: 0x0536 [0x03] Work_Zone_1700[8] = ExtData[1]->WorkLocal[17]
 34: 0x053B [0x03] ExtData[1]->WorkLocal[0] = 0*
 35: 0x0540 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=0*, condition_work_offset=1*)
 36: 0x0547 [0x02] IF !(ExtData[1]->WorkLocal[3] <= 0*) GOTO 0x0556
 37: 0x054F [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=1*, condition_work_offset=1*)
 38: 0x0556 [0x02] IF !(ExtData[1]->WorkLocal[5] <= 0*) GOTO 0x0565
 39: 0x055E [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=2*, condition_work_offset=1*)
 40: 0x0565 [0x02] IF !(ExtData[1]->WorkLocal[7] <= 0*) GOTO 0x0574
 41: 0x056D [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=3*, condition_work_offset=1*)
 42: 0x0574 [0x02] IF !(ExtData[1]->WorkLocal[9] <= 0*) GOTO 0x0583
 43: 0x057C [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=4*, condition_work_offset=1*)
 44: 0x0583 [0x02] IF !(ExtData[1]->WorkLocal[11] <= 0*) GOTO 0x0592
 45: 0x058B [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=5*, condition_work_offset=1*)
 46: 0x0592 [0x02] IF !(ExtData[1]->WorkLocal[13] <= 0*) GOTO 0x05A1
 47: 0x059A [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=6*, condition_work_offset=1*)
 48: 0x05A1 [0x02] IF !(ExtData[1]->WorkLocal[15] <= 0*) GOTO 0x05B0
 49: 0x05A9 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=7*, condition_work_offset=1*)
 50: 0x05B0 [0x02] IF !(ExtData[1]->WorkLocal[17] <= 0*) GOTO 0x05BF
 51: 0x05B8 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=8*, condition_work_offset=1*)
 52: 0x05BF [0x03] ExtData[1]->WorkLocal[1] = 4294967295*
 53: 0x05C4 [0x0F] ExtData[1]->WorkLocal[1] ^= ExtData[1]->WorkLocal[0]
 54: 0x05C9 [0x24] CREATE_DIALOG(message_id=7247*, default_option=0*, option_flags=ExtData[1]->WorkLocal[1])
    → "What do you take? [Nothing./$1 ($2 remaining)/$3 ($4 remaining)/$5 ($6 remaining)/$7 ($8 remaining)/$9 ($10 remaining)/$11 ($12 remaining)/$13 ($14 remaining)/$15 ($16 remaining)]"
 55: 0x05D0 [0x25] WAIT_DIALOG_SELECT()
 56: 0x05D1 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x05E1
 57: 0x05D9 [0x03] Work_Zone[1] = 0*
 58: 0x05DE [0x01] GOTO 0x0661
 59: 0x05E1 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x05F1
 60: 0x05E9 [0x03] Work_Zone[1] = 1*
 61: 0x05EE [0x01] GOTO 0x0661
 62: 0x05F1 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0601
 63: 0x05F9 [0x03] Work_Zone[1] = 2*
 64: 0x05FE [0x01] GOTO 0x0661
 65: 0x0601 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0611
 66: 0x0609 [0x03] Work_Zone[1] = 3*
 67: 0x060E [0x01] GOTO 0x0661
 68: 0x0611 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x0621
 69: 0x0619 [0x03] Work_Zone[1] = 4*
 70: 0x061E [0x01] GOTO 0x0661
 71: 0x0621 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x0631
 72: 0x0629 [0x03] Work_Zone[1] = 5*
 73: 0x062E [0x01] GOTO 0x0661
 74: 0x0631 [0x02] IF !(Work_Zone[0] == 6*) GOTO 0x0641
 75: 0x0639 [0x03] Work_Zone[1] = 6*
 76: 0x063E [0x01] GOTO 0x0661
 77: 0x0641 [0x02] IF !(Work_Zone[0] == 7*) GOTO 0x0651
 78: 0x0649 [0x03] Work_Zone[1] = 7*
 79: 0x064E [0x01] GOTO 0x0661
 80: 0x0651 [0x02] IF !(Work_Zone[0] == 8*) GOTO 0x0661
 81: 0x0659 [0x03] Work_Zone[1] = 8*
 82: 0x065E [0x01] GOTO 0x0661

SUBROUTINE_0661:
 83: 0x0661 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 84: 0x0662 [0x21] END_EVENT
 85: 0x0663 [0x00] END_REQSTACK()
```
