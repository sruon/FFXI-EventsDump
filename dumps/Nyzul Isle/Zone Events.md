# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value               |
|------------------|---------------------|
| Zone             | Nyzul Isle (ID: 77) |
| Block Size       | 1332 bytes          |
| Total Events     | 14                  |
| References Count | 25                  |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [65534](#event-65534) | 0x0001       |      1 |              1 |
| [0](#event-0)         | 0x0002       |     26 |              7 |
| [1](#event-1)         | 0x001C       |     46 |              9 |
| [204](#event-204)     | 0x004A       |     35 |              5 |
| [30](#event-30)       | 0x006D       |      9 |              4 |
| [50](#event-50)       | 0x0076       |     55 |             11 |
| [51](#event-51)       | 0x00AD       |     55 |             11 |
| [90](#event-90)       | 0x00E4       |     41 |              5 |
| [91](#event-91)       | 0x010D       |     38 |              4 |
| [95](#event-95)       | 0x0133       |    108 |             16 |
| [300](#event-300)     | 0x019F       |    135 |             19 |
| [2](#event-2)         | 0x0226       |    526 |             86 |
| [3](#event-3)         | 0x0434       |     82 |             23 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C8      |         200 |
|       1 | 0x0000      |           0 |
|       2 | 0x003C      |          60 |
|       3 | 0x00C9      |         201 |
|       4 | 0x008C      |         140 |
|       5 | 0x0001      |           1 |
|       6 | 0x00CA      |         202 |
|       7 | 0x0002      |           2 |
|       8 | 0x00AA      |         170 |
|       9 | 0x001E      |          30 |
|      10 | 0x00E7      |         231 |
|      11 | 0x0078      |         120 |
|      12 | 0x0008      |           8 |
|      13 | 0x000A      |          10 |
|      14 | 0x000F      |          15 |
|      15 | 0x0010      |          16 |
|      16 | 0x001F      |          31 |
|      17 | 0x0003      |           3 |
|      18 | 0x0004      |           4 |
|      19 | 0x0005      |           5 |
|      20 | 0x0006      |           6 |
|      21 | 0x0007      |           7 |
|      22 | 0xFFFFFFFF  |  4294967295 |
|      23 | 0x1CBE      |        7358 |
|      24 | 0x1CC4      |        7364 |

## String References

- **7358**: What do you take? [Nothing./$1 ($2 remaining)/$3 ($4 remaining)/$5 ($6 remaining)/$7 ($8 remaining)/$9 ($10 remaining)/$11 ($12 remaining)/$13 ($14 remaining)/$15 ($16 remaining)]
- **7364**: Activate the lamp? [Yes./Yes./No.]

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

### Event 204

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004A   |
| Data Size    | 35 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                42 45 00 80 F0 FF            BE....
0050: FF 7F F0 FF FF 7F 66 64  6F 31 01 80 55 00 80 F0  ......fdo1..U...
0060: FF FF 7F F0 FF FF 7F 66  64 6F 31 21 00           .......fdo1!.   
```

#### Opcodes

```
  0: 0x004A [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x004B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  2: 0x005C [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
  3: 0x006B [0x21] END_EVENT
  4: 0x006C [0x00] END_REQSTACK()
```

### Event 30

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x006D  |
| Data Size    | 9 bytes |
| Instructions | 4       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                         20 01 03                ..
0070: 01 10 05 80 21 00                                 ....!.          
```

#### Opcodes

```
  0: 0x006D [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x006F [0x03] Work_Zone[1] = 1*
  2: 0x0074 [0x21] END_EVENT
  3: 0x0075 [0x00] END_REQSTACK()
```

### Event 50

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0076   |
| Data Size    | 55 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                   20 01  42 43 00 43 01 45 00 80         .BC.C.E..
0080: F0 FF FF 7F F0 FF FF 7F  66 64 6F 31 01 80 1C 02  ........fdo1....
0090: 80 29 01 30 D3 04 01 01  45 00 80 F0 FF FF 7F F0  .).0....E.......
00A0: FF FF 7F 66 64 69 31 01  80 20 00 21 00           ...fdi1.. .!.   
```

#### Opcodes

```
  0: 0x0076 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0078 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0079 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  3: 0x007B [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  4: 0x007D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  5: 0x008E [0x1C] WAIT(60* ticks)
  6: 0x0091 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Weather (ID: 17093424/0x0104D330), tag_num=0x01)
  7: 0x0098 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  8: 0x00A9 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  9: 0x00AB [0x21] END_EVENT
 10: 0x00AC [0x00] END_REQSTACK()
```

### Event 51

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AD   |
| Data Size    | 55 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                         20 01 42                .B
00B0: 43 00 43 01 45 00 80 F0  FF FF 7F F0 FF FF 7F 66  C.C.E..........f
00C0: 64 6F 31 01 80 1C 02 80  29 01 30 D3 04 01 02 45  do1.....).0....E
00D0: 00 80 F0 FF FF 7F F0 FF  FF 7F 66 64 69 31 01 80  ..........fdi1..
00E0: 20 00 21 00                                        .!.            
```

#### Opcodes

```
  0: 0x00AD [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x00AF [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x00B0 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  3: 0x00B2 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  4: 0x00B4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  5: 0x00C5 [0x1C] WAIT(60* ticks)
  6: 0x00C8 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Weather (ID: 17093424/0x0104D330), tag_num=0x02)
  7: 0x00CF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  8: 0x00E0 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  9: 0x00E2 [0x21] END_EVENT
 10: 0x00E3 [0x00] END_REQSTACK()
```

### Event 90

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E4   |
| Data Size    | 41 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:             9F 06 80 F8  FF FF 7F F8 FF FF 7F 6D      ...........m
00F0: 61 69 6E 01 80 1C 04 80  45 00 80 F0 FF FF 7F F0  ain.....E.......
0100: FF FF 7F 66 64 6F 31 01  80 1C 02 80 00           ...fdo1......   
```

#### Opcodes

```
  0: 0x00E4 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [EventEntity, EventEntity], work=[202*, 0*]
  1: 0x00F5 [0x1C] WAIT(140* ticks)
  2: 0x00F8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  3: 0x0109 [0x1C] WAIT(60* ticks)
  4: 0x010C [0x00] END_REQSTACK()
```

### Event 91

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010D   |
| Data Size    | 38 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                         45 00 80               E..
0110: F0 FF FF 7F F0 FF FF 7F  66 64 69 31 01 80 62 07  ........fdi1..b.
0120: 80 F0 FF FF 7F F0 FF FF  7F 6D 61 69 6E 01 80 1C  .........main...
0130: 08 80 00                                          ...             
```

#### Opcodes

```
  0: 0x010D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  1: 0x011E [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[2*, 0*]
  2: 0x012F [0x1C] WAIT(170* ticks)
  3: 0x0132 [0x00] END_REQSTACK()
```

### Event 95

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0133    |
| Data Size    | 108 bytes |
| Instructions | 16        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:          42 9F 06 80 F8  FF FF 7F F8 FF FF 7F 6D     B...........m
0140: 61 69 6E 01 80 1C 04 80  45 00 80 F0 FF FF 7F F0  ain.....E.......
0150: FF FF 7F 66 64 6F 31 01  80 1C 02 80 3E 02 10 09  ...fdo1.....>...
0160: 80 6D 01 29 01 30 D3 04  01 01 01 74 01 29 01 30  .m.).0.....t.).0
0170: D3 04 01 02 43 00 43 01  45 00 80 F0 FF FF 7F F0  ....C.C.E.......
0180: FF FF 7F 66 64 69 31 01  80 9F 0A 80 F8 FF FF 7F  ...fdi1.........
0190: F8 FF FF 7F 6D 61 69 6E  01 80 1C 0B 80 21 00     ....main.....!. 
```

#### Opcodes

```
  0: 0x0133 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0134 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [EventEntity, EventEntity], work=[202*, 0*]
  2: 0x0145 [0x1C] WAIT(140* ticks)
  3: 0x0148 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x0159 [0x1C] WAIT(60* ticks)
  5: 0x015C [0x3E] IF !(Work_Zone[2] bit 30*) GOTO 0x016D
  6: 0x0163 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Weather (ID: 17093424/0x0104D330), tag_num=0x01)
  7: 0x016A [0x01] GOTO 0x0174
  8: 0x016D [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Weather (ID: 17093424/0x0104D330), tag_num=0x02)

SUBROUTINE_0174:
  9: 0x0174 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 10: 0x0176 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 11: 0x0178 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 12: 0x0189 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [EventEntity, EventEntity], work=[231*, 0*]
 13: 0x019A [0x1C] WAIT(120* ticks)
 14: 0x019D [0x21] END_EVENT
 15: 0x019E [0x00] END_REQSTACK()
```

### Event 300

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x019F    |
| Data Size    | 135 bytes |
| Instructions | 19        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                                               42                 B
01A0: 9F 06 80 F8 FF FF 7F F8  FF FF 7F 6D 61 69 6E 01  ...........main.
01B0: 80 1C 04 80 45 00 80 F0  FF FF 7F F0 FF FF 7F 66  ....E..........f
01C0: 64 6F 31 01 80 1C 02 80  02 02 10 0C 80 80 DA 01  do1.............
01D0: 29 01 30 D3 04 01 01 01  F3 01 02 02 10 0D 80 80  ).0.............
01E0: EC 01 29 01 30 D3 04 01  01 01 F3 01 29 01 30 D3  ..).0.......).0.
01F0: 04 01 02 47 00 03 10 04  10 05 10 06 10 47 01 45  ...G.........G.E
0200: 00 80 F0 FF FF 7F F0 FF  FF 7F 66 64 69 31 01 80  ..........fdi1..
0210: 9F 0A 80 F8 FF FF 7F F8  FF FF 7F 6D 61 69 6E 01  ...........main.
0220: 80 1C 0B 80 21 00                                 ....!.          
```

#### Opcodes

```
  0: 0x019F [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x01A0 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [EventEntity, EventEntity], work=[202*, 0*]
  2: 0x01B1 [0x1C] WAIT(140* ticks)
  3: 0x01B4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x01C5 [0x1C] WAIT(60* ticks)
  5: 0x01C8 [0x02] IF !(Work_Zone[2] == 8*) GOTO 0x01DA
  6: 0x01D0 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Weather (ID: 17093424/0x0104D330), tag_num=0x01)
  7: 0x01D7 [0x01] GOTO 0x01F3
  8: 0x01DA [0x02] IF !(Work_Zone[2] == 10*) GOTO 0x01EC
  9: 0x01E2 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Weather (ID: 17093424/0x0104D330), tag_num=0x01)
 10: 0x01E9 [0x01] GOTO 0x01F3
 11: 0x01EC [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Weather (ID: 17093424/0x0104D330), tag_num=0x02)

SUBROUTINE_01F3:
 12: 0x01F3 [0x47] UPDATE_PLAYER_POS(Work_Zone[3], Work_Zone[4], Work_Zone[5], yaw=Work_Zone[6])
 13: 0x01FD [0x47] WAIT_PLAYER_POS_UPDATE
 14: 0x01FF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 15: 0x0210 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [EventEntity, EventEntity], work=[231*, 0*]
 16: 0x0221 [0x1C] WAIT(120* ticks)
 17: 0x0224 [0x21] END_EVENT
 18: 0x0225 [0x00] END_REQSTACK()
```

### Event 2

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0226    |
| Data Size    | 526 bytes |
| Instructions | 86        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0220:                   20 01  1C 02 80 41 01 80 0E 80         ....A....
0230: 02 10 02 00 41 0F 80 10  80 02 10 03 00 41 01 80  ....A........A..
0240: 0E 80 03 10 04 00 41 0F  80 10 80 03 10 05 00 41  ......A........A
0250: 01 80 0E 80 04 10 06 00  41 0F 80 10 80 04 10 07  ........A.......
0260: 00 41 01 80 0E 80 05 10  08 00 41 0F 80 10 80 05  .A........A.....
0270: 10 09 00 41 01 80 0E 80  06 10 0A 00 41 0F 80 10  ...A........A...
0280: 80 06 10 0B 00 41 01 80  0E 80 07 10 0C 00 41 0F  .....A........A.
0290: 80 10 80 07 10 0D 00 41  01 80 0E 80 08 10 0E 00  .......A........
02A0: 41 0F 80 10 80 08 10 0F  00 41 01 80 0E 80 09 10  A........A......
02B0: 10 00 41 0F 80 10 80 09  10 11 00 03 03 10 02 00  ..A.............
02C0: 03 04 10 03 00 03 05 10  04 00 03 06 10 05 00 03  ................
02D0: 07 10 06 00 03 08 10 07  00 03 09 10 08 00 03 00  ................
02E0: 17 09 00 03 01 17 0A 00  03 02 17 0B 00 03 03 17  ................
02F0: 0C 00 03 04 17 0D 00 03  05 17 0E 00 03 06 17 0F  ................
0300: 00 03 07 17 10 00 03 08  17 11 00 03 00 00 01 80  ................
0310: 3C 00 00 01 80 05 80 02  03 00 01 80 02 26 03 3C  <............&.<
0320: 00 00 05 80 05 80 02 05  00 01 80 02 35 03 3C 00  ............5.<.
0330: 00 07 80 05 80 02 07 00  01 80 02 44 03 3C 00 00  ...........D.<..
0340: 11 80 05 80 02 09 00 01  80 02 53 03 3C 00 00 12  ..........S.<...
0350: 80 05 80 02 0B 00 01 80  02 62 03 3C 00 00 13 80  .........b.<....
0360: 05 80 02 0D 00 01 80 02  71 03 3C 00 00 14 80 05  ........q.<.....
0370: 80 02 0F 00 01 80 02 80  03 3C 00 00 15 80 05 80  .........<......
0380: 02 11 00 01 80 02 8F 03  3C 00 00 0C 80 05 80 03  ........<.......
0390: 01 00 16 80 0F 01 00 00  00 24 17 80 01 80 01 00  .........$......
03A0: 25 02 00 10 01 80 00 B1  03 03 01 10 01 80 01 31  %..............1
03B0: 04 02 00 10 05 80 00 C1  03 03 01 10 05 80 01 31  ...............1
03C0: 04 02 00 10 07 80 00 D1  03 03 01 10 07 80 01 31  ...............1
03D0: 04 02 00 10 11 80 00 E1  03 03 01 10 11 80 01 31  ...............1
03E0: 04 02 00 10 12 80 00 F1  03 03 01 10 12 80 01 31  ...............1
03F0: 04 02 00 10 13 80 00 01  04 03 01 10 13 80 01 31  ...............1
0400: 04 02 00 10 14 80 00 11  04 03 01 10 14 80 01 31  ...............1
0410: 04 02 00 10 15 80 00 21  04 03 01 10 15 80 01 31  .......!.......1
0420: 04 02 00 10 0C 80 00 31  04 03 01 10 0C 80 01 31  .......1.......1
0430: 04 42 21 00                                       .B!.            
```

#### Opcodes

```
  0: 0x0226 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0228 [0x1C] WAIT(60* ticks)
  2: 0x022B [0x41] ExtData[1]->WorkLocal[2] = Work_Zone[2] (bits 0*-15*)
  3: 0x0234 [0x41] ExtData[1]->WorkLocal[3] = Work_Zone[2] (bits 16*-31*)
  4: 0x023D [0x41] ExtData[1]->WorkLocal[4] = Work_Zone[3] (bits 0*-15*)
  5: 0x0246 [0x41] ExtData[1]->WorkLocal[5] = Work_Zone[3] (bits 16*-31*)
  6: 0x024F [0x41] ExtData[1]->WorkLocal[6] = Work_Zone[4] (bits 0*-15*)
  7: 0x0258 [0x41] ExtData[1]->WorkLocal[7] = Work_Zone[4] (bits 16*-31*)
  8: 0x0261 [0x41] ExtData[1]->WorkLocal[8] = Work_Zone[5] (bits 0*-15*)
  9: 0x026A [0x41] ExtData[1]->WorkLocal[9] = Work_Zone[5] (bits 16*-31*)
 10: 0x0273 [0x41] ExtData[1]->WorkLocal[10] = Work_Zone[6] (bits 0*-15*)
 11: 0x027C [0x41] ExtData[1]->WorkLocal[11] = Work_Zone[6] (bits 16*-31*)
 12: 0x0285 [0x41] ExtData[1]->WorkLocal[12] = Work_Zone[7] (bits 0*-15*)
 13: 0x028E [0x41] ExtData[1]->WorkLocal[13] = Work_Zone[7] (bits 16*-31*)
 14: 0x0297 [0x41] ExtData[1]->WorkLocal[14] = Work_Zone[8] (bits 0*-15*)
 15: 0x02A0 [0x41] ExtData[1]->WorkLocal[15] = Work_Zone[8] (bits 16*-31*)
 16: 0x02A9 [0x41] ExtData[1]->WorkLocal[16] = Work_Zone[9] (bits 0*-15*)
 17: 0x02B2 [0x41] ExtData[1]->WorkLocal[17] = Work_Zone[9] (bits 16*-31*)
 18: 0x02BB [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[2]
 19: 0x02C0 [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[3]
 20: 0x02C5 [0x03] Work_Zone[5] = ExtData[1]->WorkLocal[4]
 21: 0x02CA [0x03] Work_Zone[6] = ExtData[1]->WorkLocal[5]
 22: 0x02CF [0x03] Work_Zone[7] = ExtData[1]->WorkLocal[6]
 23: 0x02D4 [0x03] Work_Zone[8] = ExtData[1]->WorkLocal[7]
 24: 0x02D9 [0x03] Work_Zone[9] = ExtData[1]->WorkLocal[8]
 25: 0x02DE [0x03] Work_Zone_1700[0] = ExtData[1]->WorkLocal[9]
 26: 0x02E3 [0x03] Work_Zone_1700[1] = ExtData[1]->WorkLocal[10]
 27: 0x02E8 [0x03] Work_Zone_1700[2] = ExtData[1]->WorkLocal[11]
 28: 0x02ED [0x03] Work_Zone_1700[3] = ExtData[1]->WorkLocal[12]
 29: 0x02F2 [0x03] Work_Zone_1700[4] = ExtData[1]->WorkLocal[13]
 30: 0x02F7 [0x03] Work_Zone_1700[5] = ExtData[1]->WorkLocal[14]
 31: 0x02FC [0x03] Work_Zone_1700[6] = ExtData[1]->WorkLocal[15]
 32: 0x0301 [0x03] Work_Zone_1700[7] = ExtData[1]->WorkLocal[16]
 33: 0x0306 [0x03] Work_Zone_1700[8] = ExtData[1]->WorkLocal[17]
 34: 0x030B [0x03] ExtData[1]->WorkLocal[0] = 0*
 35: 0x0310 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=0*, condition_work_offset=1*)
 36: 0x0317 [0x02] IF !(ExtData[1]->WorkLocal[3] <= 0*) GOTO 0x0326
 37: 0x031F [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=1*, condition_work_offset=1*)
 38: 0x0326 [0x02] IF !(ExtData[1]->WorkLocal[5] <= 0*) GOTO 0x0335
 39: 0x032E [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=2*, condition_work_offset=1*)
 40: 0x0335 [0x02] IF !(ExtData[1]->WorkLocal[7] <= 0*) GOTO 0x0344
 41: 0x033D [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=3*, condition_work_offset=1*)
 42: 0x0344 [0x02] IF !(ExtData[1]->WorkLocal[9] <= 0*) GOTO 0x0353
 43: 0x034C [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=4*, condition_work_offset=1*)
 44: 0x0353 [0x02] IF !(ExtData[1]->WorkLocal[11] <= 0*) GOTO 0x0362
 45: 0x035B [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=5*, condition_work_offset=1*)
 46: 0x0362 [0x02] IF !(ExtData[1]->WorkLocal[13] <= 0*) GOTO 0x0371
 47: 0x036A [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=6*, condition_work_offset=1*)
 48: 0x0371 [0x02] IF !(ExtData[1]->WorkLocal[15] <= 0*) GOTO 0x0380
 49: 0x0379 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=7*, condition_work_offset=1*)
 50: 0x0380 [0x02] IF !(ExtData[1]->WorkLocal[17] <= 0*) GOTO 0x038F
 51: 0x0388 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=8*, condition_work_offset=1*)
 52: 0x038F [0x03] ExtData[1]->WorkLocal[1] = 4294967295*
 53: 0x0394 [0x0F] ExtData[1]->WorkLocal[1] ^= ExtData[1]->WorkLocal[0]
 54: 0x0399 [0x24] CREATE_DIALOG(message_id=7358*, default_option=0*, option_flags=ExtData[1]->WorkLocal[1])
    → "What do you take? [Nothing./$1 ($2 remaining)/$3 ($4 remaining)/$5 ($6 remaining)/$7 ($8 remaining)/$9 ($10 remaining)/$11 ($12 remaining)/$13 ($14 remaining)/$15 ($16 remaining)]"
 55: 0x03A0 [0x25] WAIT_DIALOG_SELECT()
 56: 0x03A1 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x03B1
 57: 0x03A9 [0x03] Work_Zone[1] = 0*
 58: 0x03AE [0x01] GOTO 0x0431
 59: 0x03B1 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x03C1
 60: 0x03B9 [0x03] Work_Zone[1] = 1*
 61: 0x03BE [0x01] GOTO 0x0431
 62: 0x03C1 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x03D1
 63: 0x03C9 [0x03] Work_Zone[1] = 2*
 64: 0x03CE [0x01] GOTO 0x0431
 65: 0x03D1 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x03E1
 66: 0x03D9 [0x03] Work_Zone[1] = 3*
 67: 0x03DE [0x01] GOTO 0x0431
 68: 0x03E1 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x03F1
 69: 0x03E9 [0x03] Work_Zone[1] = 4*
 70: 0x03EE [0x01] GOTO 0x0431
 71: 0x03F1 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x0401
 72: 0x03F9 [0x03] Work_Zone[1] = 5*
 73: 0x03FE [0x01] GOTO 0x0431
 74: 0x0401 [0x02] IF !(Work_Zone[0] == 6*) GOTO 0x0411
 75: 0x0409 [0x03] Work_Zone[1] = 6*
 76: 0x040E [0x01] GOTO 0x0431
 77: 0x0411 [0x02] IF !(Work_Zone[0] == 7*) GOTO 0x0421
 78: 0x0419 [0x03] Work_Zone[1] = 7*
 79: 0x041E [0x01] GOTO 0x0431
 80: 0x0421 [0x02] IF !(Work_Zone[0] == 8*) GOTO 0x0431
 81: 0x0429 [0x03] Work_Zone[1] = 8*
 82: 0x042E [0x01] GOTO 0x0431

SUBROUTINE_0431:
 83: 0x0431 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 84: 0x0432 [0x21] END_EVENT
 85: 0x0433 [0x00] END_REQSTACK()
```

### Event 3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0434   |
| Data Size    | 82 bytes |
| Instructions | 23       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0430:             20 01 03 12  00 02 10 03 13 00 16 80       ...........
0440: 0F 13 00 12 00 24 18 80  07 80 13 00 25 02 00 10  .....$......%...
0450: 01 80 00 62 04 43 00 43  01 42 03 01 10 05 80 01  ...b.C.C.B......
0460: 82 04 02 00 10 05 80 00  77 04 43 00 43 01 42 03  ........w.C.C.B.
0470: 01 10 07 80 01 82 04 02  00 10 07 80 00 82 04 01  ................
0480: 82 04 20 00 21 00                                 .. .!.          
```

#### Opcodes

```
  0: 0x0434 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0436 [0x03] ExtData[1]->WorkLocal[18] = Work_Zone[2]
  2: 0x043B [0x03] ExtData[1]->WorkLocal[19] = 4294967295*
  3: 0x0440 [0x0F] ExtData[1]->WorkLocal[19] ^= ExtData[1]->WorkLocal[18]
  4: 0x0445 [0x24] CREATE_DIALOG(message_id=7364*, default_option=2*, option_flags=ExtData[1]->WorkLocal[19])
    → "Activate the lamp? [Yes./Yes./No.]"
  5: 0x044C [0x25] WAIT_DIALOG_SELECT()
  6: 0x044D [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0462
  7: 0x0455 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  8: 0x0457 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  9: 0x0459 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 10: 0x045A [0x03] Work_Zone[1] = 1*
 11: 0x045F [0x01] GOTO 0x0482
 12: 0x0462 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0477
 13: 0x046A [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 14: 0x046C [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 15: 0x046E [0x42] SET_CLI_EVENT_CANCEL_DATA()
 16: 0x046F [0x03] Work_Zone[1] = 2*
 17: 0x0474 [0x01] GOTO 0x0482
 18: 0x0477 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0482
 19: 0x047F [0x01] GOTO 0x0482

SUBROUTINE_0482:
 20: 0x0482 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 21: 0x0484 [0x21] END_EVENT
 22: 0x0485 [0x00] END_REQSTACK()
```
