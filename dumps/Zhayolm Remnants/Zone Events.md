# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Zhayolm Remnants (ID: 73) |
| Block Size       | 1604 bytes                |
| Total Events     | 23                        |
| References Count | 33                        |

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
| [207](#event-207)     | 0x036B       |     72 |             18 |
| [208](#event-208)     | 0x03B3       |    107 |             24 |
| [209](#event-209)     | 0x041E       |     72 |             18 |
| [210](#event-210)     | 0x0466       |     79 |             19 |
| [211](#event-211)     | 0x04B5       |     46 |             14 |
| [212](#event-212)     | 0x04E3       |     79 |             19 |
| [300](#event-300)     | 0x0532       |     31 |             10 |

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
|      12 | 0x668A0     |      420000 |
|      13 | 0x4FED      |       20461 |
|      14 | 0xFFFFFE0D  |  4294966797 |
|      15 | 0x0C00      |        3072 |
|      16 | 0xFFFDDD20  |  4294827296 |
|      17 | 0x3F7A0     |      260000 |
|      18 | 0x4E20      |       20000 |
|      19 | 0x53020     |      340000 |
|      20 | 0x704E0     |      460000 |
|      21 | 0xFFFFFE0C  |  4294966796 |
|      22 | 0xFFFACFE0  |  4294627296 |
|      23 | 0xFFF72660  |  4294387296 |
|      24 | 0xFFF85EE0  |  4294467296 |
|      25 | 0x0400      |        1024 |
|      26 | 0xFFFA33A0  |  4294587296 |
|      27 | 0xFFFD40E0  |  4294787296 |
|      28 | 0xFFFB6C20  |  4294667296 |
|      29 | 0xFFFFB1E0  |  4294947296 |
|      30 | 0x0002      |           2 |
|      31 | 0x35B60     |      220000 |
|      32 | 0x1D12      |        7442 |

## String References

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
00B0: 80 1C 02 80 29 01 E9 92  04 01 01 45 00 80 F0 FF  ....)......E....
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
  6: 0x00B4 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Weather (ID: 17076969/0x010492E9), tag_num=0x01)
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
00E0: FF 7F 66 64 6F 31 01 80  1C 02 80 29 01 E9 92 04  ..fdo1.....)....
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
  6: 0x00EB [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Weather (ID: 17076969/0x010492E9), tag_num=0x02)
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
0130: 3E 02 10 08 80 41 01 29  01 E9 92 04 01 01 01 48  >....A.).......H
0140: 01 29 01 E9 92 04 01 02  43 00 43 01 45 00 80 F0  .)......C.C.E...
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
  6: 0x0137 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Weather (ID: 17076969/0x010492E9), tag_num=0x01)
  7: 0x013E [0x01] GOTO 0x0148
  8: 0x0141 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Weather (ID: 17076969/0x010492E9), tag_num=0x02)

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
  9: 0x0196 [0x47] UPDATE_PLAYER_POS(420.000*, 20.461*, -0.499*, yaw=270.0°*)
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
01E0: 0C 80 10 80 0E 80 0F 80  47 01 29 01 F0 FF FF 7F  ........G.).....
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
  9: 0x01DE [0x47] UPDATE_PLAYER_POS(420.000*, -140.000*, -0.499*, yaw=270.0°*)
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
0220: 01 F0 FF FF 7F 04 47 00  11 80 10 80 0E 80 0F 80  ......G.........
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
  9: 0x0226 [0x47] UPDATE_PLAYER_POS(260.000*, -140.000*, -0.499*, yaw=270.0°*)
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
0270: 11 80 12 80 0E 80 0F 80  47 01 29 01 F0 FF FF 7F  ........G.).....
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
  9: 0x026E [0x47] UPDATE_PLAYER_POS(260.000*, 20.000*, -0.499*, yaw=270.0°*)
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
02B0: 01 F0 FF FF 7F 04 47 00  13 80 14 80 15 80 0F 80  ......G.........
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
  9: 0x02B6 [0x47] UPDATE_PLAYER_POS(340.000*, 460.000*, -0.500*, yaw=270.0°*)
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
0300: 16 80 17 80 0E 80 0F 80  47 01 29 01 F0 FF FF 7F  ........G.).....
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
  9: 0x02FE [0x47] UPDATE_PLAYER_POS(-340.000*, -580.000*, -0.499*, yaw=270.0°*)
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
0340: 01 F0 FF FF 7F 04 47 00  16 80 18 80 0E 80 19 80  ......G.........
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
  9: 0x0346 [0x47] UPDATE_PLAYER_POS(-340.000*, -500.000*, -0.499*, yaw=90.0°*)
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
| Data Size    | 72 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0360:                                   20 01 24 0A 80              .$..
0370: 0B 80 01 80 25 02 00 10  01 80 00 A4 03 42 43 00  ....%........BC.
0380: 43 01 03 01 10 0B 80 29  01 F0 FF FF 7F 04 47 00  C......)......G.
0390: 1A 80 1B 80 15 80 19 80  47 01 29 01 F0 FF FF 7F  ........G.).....
03A0: 05 01 AF 03 02 00 10 0B  80 00 AF 03 01 AF 03 20  ............... 
03B0: 00 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x036B [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x036D [0x24] CREATE_DIALOG(message_id=7440*, default_option=1*, option_flags=0*)
    → "Use the device? [Yes./No.]"
  2: 0x0374 [0x25] WAIT_DIALOG_SELECT()
  3: 0x0375 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x03A4
  4: 0x037D [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x037E [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  6: 0x0380 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  7: 0x0382 [0x03] Work_Zone[1] = 1*
  8: 0x0387 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
  9: 0x038E [0x47] UPDATE_PLAYER_POS(-380.000*, -180.000*, -0.500*, yaw=90.0°*)
 10: 0x0398 [0x47] WAIT_PLAYER_POS_UPDATE
 11: 0x039A [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x05)
 12: 0x03A1 [0x01] GOTO 0x03AF
 13: 0x03A4 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x03AF
 14: 0x03AC [0x01] GOTO 0x03AF

SUBROUTINE_03AF:
 15: 0x03AF [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 16: 0x03B1 [0x21] END_EVENT
 17: 0x03B2 [0x00] END_REQSTACK()
```

### Event 208

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x03B3    |
| Data Size    | 107 bytes |
| Instructions | 24        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03B0:          20 01 24 0A 80  0B 80 01 80 25 02 00 10      .$......%...
03C0: 01 80 00 0F 04 42 43 00  43 01 02 02 10 01 80 00  .....BC.C.......
03D0: ED 03 03 01 10 0B 80 29  01 F0 FF FF 7F 04 47 00  .......)......G.
03E0: 1C 80 1D 80 15 80 0F 80  47 01 01 05 04 03 01 10  ........G.......
03F0: 1E 80 29 01 F0 FF FF 7F  04 47 00 16 80 18 80 0E  ..)......G......
0400: 80 19 80 47 01 29 01 F0  FF FF 7F 05 01 1A 04 02  ...G.)..........
0410: 00 10 0B 80 00 1A 04 01  1A 04 20 00 21 00        .......... .!.  
```

#### Opcodes

```
  0: 0x03B3 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x03B5 [0x24] CREATE_DIALOG(message_id=7440*, default_option=1*, option_flags=0*)
    → "Use the device? [Yes./No.]"
  2: 0x03BC [0x25] WAIT_DIALOG_SELECT()
  3: 0x03BD [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x040F
  4: 0x03C5 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x03C6 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  6: 0x03C8 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  7: 0x03CA [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x03ED
  8: 0x03D2 [0x03] Work_Zone[1] = 1*
  9: 0x03D7 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
 10: 0x03DE [0x47] UPDATE_PLAYER_POS(-300.000*, -20.000*, -0.500*, yaw=270.0°*)
 11: 0x03E8 [0x47] WAIT_PLAYER_POS_UPDATE
 12: 0x03EA [0x01] GOTO 0x0405
 13: 0x03ED [0x03] Work_Zone[1] = 2*
 14: 0x03F2 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
 15: 0x03F9 [0x47] UPDATE_PLAYER_POS(-340.000*, -500.000*, -0.499*, yaw=90.0°*)
 16: 0x0403 [0x47] WAIT_PLAYER_POS_UPDATE

SUBROUTINE_0405:
 17: 0x0405 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x05)
 18: 0x040C [0x01] GOTO 0x041A
 19: 0x040F [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x041A
 20: 0x0417 [0x01] GOTO 0x041A

SUBROUTINE_041A:
 21: 0x041A [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 22: 0x041C [0x21] END_EVENT
 23: 0x041D [0x00] END_REQSTACK()
```

### Event 209

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x041E   |
| Data Size    | 72 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0410:                                            20 01                 .
0420: 24 0A 80 0B 80 01 80 25  02 00 10 01 80 00 57 04  $......%......W.
0430: 42 43 00 43 01 03 01 10  0B 80 29 01 F0 FF FF 7F  BC.C......).....
0440: 04 47 00 16 80 1F 80 0E  80 0F 80 47 01 29 01 F0  .G.........G.)..
0450: FF FF 7F 05 01 62 04 02  00 10 0B 80 00 62 04 01  .....b.......b..
0460: 62 04 20 00 21 00                                 b. .!.          
```

#### Opcodes

```
  0: 0x041E [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0420 [0x24] CREATE_DIALOG(message_id=7440*, default_option=1*, option_flags=0*)
    → "Use the device? [Yes./No.]"
  2: 0x0427 [0x25] WAIT_DIALOG_SELECT()
  3: 0x0428 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0457
  4: 0x0430 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x0431 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  6: 0x0433 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  7: 0x0435 [0x03] Work_Zone[1] = 1*
  8: 0x043A [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
  9: 0x0441 [0x47] UPDATE_PLAYER_POS(-340.000*, 220.000*, -0.499*, yaw=270.0°*)
 10: 0x044B [0x47] WAIT_PLAYER_POS_UPDATE
 11: 0x044D [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x05)
 12: 0x0454 [0x01] GOTO 0x0462
 13: 0x0457 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0462
 14: 0x045F [0x01] GOTO 0x0462

SUBROUTINE_0462:
 15: 0x0462 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 16: 0x0464 [0x21] END_EVENT
 17: 0x0465 [0x00] END_REQSTACK()
```

### Event 210

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0466   |
| Data Size    | 79 bytes |
| Instructions | 19       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0460:                   20 01  24 0A 80 0B 80 01 80 25         .$......%
0470: 02 00 10 01 80 00 A6 04  42 43 00 43 01 03 01 10  ........BC.C....
0480: 0B 80 29 01 F0 FF FF 7F  04 47 00 16 80 14 80 0E  ..)......G......
0490: 80 0F 80 47 01 29 01 E9  92 04 01 01 29 01 F0 FF  ...G.)......)...
04A0: FF 7F 05 01 B1 04 02 00  10 0B 80 00 B1 04 01 B1  ................
04B0: 04 20 00 21 00                                    . .!.           
```

#### Opcodes

```
  0: 0x0466 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0468 [0x24] CREATE_DIALOG(message_id=7440*, default_option=1*, option_flags=0*)
    → "Use the device? [Yes./No.]"
  2: 0x046F [0x25] WAIT_DIALOG_SELECT()
  3: 0x0470 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x04A6
  4: 0x0478 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x0479 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  6: 0x047B [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  7: 0x047D [0x03] Work_Zone[1] = 1*
  8: 0x0482 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
  9: 0x0489 [0x47] UPDATE_PLAYER_POS(-340.000*, 460.000*, -0.499*, yaw=270.0°*)
 10: 0x0493 [0x47] WAIT_PLAYER_POS_UPDATE
 11: 0x0495 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Weather (ID: 17076969/0x010492E9), tag_num=0x01)
 12: 0x049C [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x05)
 13: 0x04A3 [0x01] GOTO 0x04B1
 14: 0x04A6 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x04B1
 15: 0x04AE [0x01] GOTO 0x04B1

SUBROUTINE_04B1:
 16: 0x04B1 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 17: 0x04B3 [0x21] END_EVENT
 18: 0x04B4 [0x00] END_REQSTACK()
```

### Event 211

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x04B5   |
| Data Size    | 46 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
04B0:                20 01 24  0A 80 0B 80 01 80 25 02        .$......%.
04C0: 00 10 01 80 00 D4 04 42  43 00 43 01 03 01 10 0B  .......BC.C.....
04D0: 80 01 DF 04 02 00 10 0B  80 00 DF 04 01 DF 04 20  ............... 
04E0: 00 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x04B5 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x04B7 [0x24] CREATE_DIALOG(message_id=7440*, default_option=1*, option_flags=0*)
    → "Use the device? [Yes./No.]"
  2: 0x04BE [0x25] WAIT_DIALOG_SELECT()
  3: 0x04BF [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x04D4
  4: 0x04C7 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x04C8 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  6: 0x04CA [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  7: 0x04CC [0x03] Work_Zone[1] = 1*
  8: 0x04D1 [0x01] GOTO 0x04DF
  9: 0x04D4 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x04DF
 10: 0x04DC [0x01] GOTO 0x04DF

SUBROUTINE_04DF:
 11: 0x04DF [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 12: 0x04E1 [0x21] END_EVENT
 13: 0x04E2 [0x00] END_REQSTACK()
```

### Event 212

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x04E3   |
| Data Size    | 79 bytes |
| Instructions | 19       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
04E0:          20 01 24 0A 80  0B 80 01 80 25 02 00 10      .$......%...
04F0: 01 80 00 23 05 42 43 00  43 01 03 01 10 0B 80 29  ...#.BC.C......)
0500: 01 F0 FF FF 7F 04 47 00  0C 80 0D 80 0E 80 0F 80  ......G.........
0510: 47 01 29 01 E9 92 04 01  02 29 01 F0 FF FF 7F 05  G.)......)......
0520: 01 2E 05 02 00 10 0B 80  00 2E 05 01 2E 05 20 00  .............. .
0530: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x04E3 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x04E5 [0x24] CREATE_DIALOG(message_id=7440*, default_option=1*, option_flags=0*)
    → "Use the device? [Yes./No.]"
  2: 0x04EC [0x25] WAIT_DIALOG_SELECT()
  3: 0x04ED [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0523
  4: 0x04F5 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x04F6 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  6: 0x04F8 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  7: 0x04FA [0x03] Work_Zone[1] = 1*
  8: 0x04FF [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
  9: 0x0506 [0x47] UPDATE_PLAYER_POS(420.000*, 20.461*, -0.499*, yaw=270.0°*)
 10: 0x0510 [0x47] WAIT_PLAYER_POS_UPDATE
 11: 0x0512 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Weather (ID: 17076969/0x010492E9), tag_num=0x02)
 12: 0x0519 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x05)
 13: 0x0520 [0x01] GOTO 0x052E
 14: 0x0523 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x052E
 15: 0x052B [0x01] GOTO 0x052E

SUBROUTINE_052E:
 16: 0x052E [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 17: 0x0530 [0x21] END_EVENT
 18: 0x0531 [0x00] END_REQSTACK()
```

### Event 300

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0532   |
| Data Size    | 31 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0530:       20 01 24 20 80 0B  80 01 80 25 02 00 10 01     .$ .....%....
0540: 80 00 4D 05 42 03 01 10  0B 80 01 4D 05 20 00 21  ..M.B......M. .!
0550: 00                                                .               
```

#### Opcodes

```
  0: 0x0532 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0534 [0x24] CREATE_DIALOG(message_id=7442*, default_option=1*, option_flags=0*)
    → "Open the door? [Yes./No.]"
  2: 0x053B [0x25] WAIT_DIALOG_SELECT()
  3: 0x053C [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x054D
  4: 0x0544 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x0545 [0x03] Work_Zone[1] = 1*
  6: 0x054A [0x01] GOTO 0x054D

SUBROUTINE_054D:
  7: 0x054D [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x054F [0x21] END_EVENT
  9: 0x0550 [0x00] END_REQSTACK()
```
