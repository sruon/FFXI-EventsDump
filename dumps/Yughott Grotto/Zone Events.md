# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Yughott Grotto (ID: 142) |
| Block Size       | 492 bytes                |
| Total Events     | 10                       |
| References Count | 23                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65534](#event-65534)    | 0x0001       |    149 |             33 |
| [65535.1](#event-655351) | 0x0096       |      6 |              2 |
| [65535.2](#event-655352) | 0x009C       |      6 |              2 |
| [65535.3](#event-655353) | 0x00A2       |      7 |              3 |
| [65535.4](#event-655354) | 0x00A9       |      7 |              3 |
| [102](#event-102)        | 0x00B0       |    102 |             15 |
| [65535.5](#event-655355) | 0x0116       |     11 |              3 |
| [65535.6](#event-655356) | 0x0121       |     38 |             10 |
| [65535.7](#event-655357) | 0x0147       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0005      |           5 |
|       1 | 0x0001      |           1 |
|       2 | 0x0002      |           2 |
|       3 | 0x000A      |          10 |
|       4 | 0x0009      |           9 |
|       5 | 0x0046      |          70 |
|       6 | 0x008C      |         140 |
|       7 | 0x00D2      |         210 |
|       8 | 0x0000      |           0 |
|       9 | 0x1CAC      |        7340 |
|      10 | 0x00C8      |         200 |
|      11 | 0x005A      |          90 |
|      12 | 0x003C      |          60 |
|      13 | 0x00C9      |         201 |
|      14 | 0x4406      |       17414 |
|      15 | 0x0D21      |        3361 |
|      16 | 0x0028      |          40 |
|      17 | 0x5DBA4     |      383908 |
|      18 | 0xFFFFF942  |  4294965570 |
|      19 | 0x2AF7      |       10999 |
|      20 | 0x5A701     |      370433 |
|      21 | 0xFFFFF22C  |  4294963756 |
|      22 | 0x27AF      |       10159 |

## String References

- **7340**: The order has been given by your party leader to enter [Everbloom Hollow/the Ruhotz Silvermines/Ghoyu's Reverie].

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

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 149 bytes |
| Instructions | 1         |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00 03 01 00 00 00 02  01 00 00 80 05 17 00 08   ...............
0010: 01 00 01 80 01 1C 00 08  01 00 02 80 14 01 00 03  ................
0020: 80 07 01 00 04 80 1B 03  01 00 00 00 02 01 00 00  ................
0030: 80 05 3C 00 08 01 00 01  80 01 41 00 08 01 00 02  ..<.......A.....
0040: 80 14 01 00 03 80 07 01  00 05 80 1B 03 01 00 00  ................
0050: 00 02 01 00 00 80 05 61  00 08 01 00 01 80 01 66  .......a.......f
0060: 00 08 01 00 02 80 14 01  00 03 80 07 01 00 06 80  ................
0070: 1B 03 01 00 00 00 02 01  00 00 80 05 86 00 08 01  ................
0080: 00 01 80 01 8B 00 08 01  00 02 80 14 01 00 03 80  ................
0090: 07 01 00 07 80 1B                                 ......          
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0002 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x0007 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x0017
     0x000F [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x0014 [0x01] GOTO 0x001C
     0x0017 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x001C [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x0021 [0x07] ExtData[1]->WorkLocal[1] += 9*
     0x0026 [0x1B] RETURN
     0x0027 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x002C [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x003C
     0x0034 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x0039 [0x01] GOTO 0x0041
     0x003C [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x0041 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x0046 [0x07] ExtData[1]->WorkLocal[1] += 70*
     0x004B [0x1B] RETURN
     0x004C [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x0051 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x0061
     0x0059 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x005E [0x01] GOTO 0x0066
     0x0061 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x0066 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x006B [0x07] ExtData[1]->WorkLocal[1] += 140*
     0x0070 [0x1B] RETURN
     0x0071 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x0076 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x0086
     0x007E [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x0083 [0x01] GOTO 0x008B
     0x0086 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x008B [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x0090 [0x07] ExtData[1]->WorkLocal[1] += 210*
     0x0095 [0x1B] RETURN
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0096  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                   03 02  10 07 7F 00                    ......    
```

#### Opcodes

```
  0: 0x0096 [0x03] Work_Zone[2] = Entity->Race
  1: 0x009B [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x009C  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                      03 02 10 0B              ....
00A0: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x009C [0x03] Work_Zone[2] = (Entity->Render.Flags01 >> 25) & 1
  1: 0x00A1 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A2  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:       AB 03 AC 01 01 80  00                         .......       
```

#### Opcodes

```
  0: 0x00A2 [0xAB] EventEntity->Render.Flags0 ^= 0x20000 // Toggle bit 17
  1: 0x00A4 [0xAC] EventEntity->StatusEvent = 1*
  2: 0x00A8 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A9  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                             AC 01 08 80 AB 04 00           .......
```

#### Opcodes

```
  0: 0x00A9 [0xAC] EventEntity->StatusEvent = 0*
  1: 0x00AD [0xAB] EventEntity->Render.Flags0 |= 0x40000 // Set bit 18
  2: 0x00AF [0x00] END_REQSTACK()
```

### Event 102

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00B0    |
| Data Size    | 102 bytes |
| Instructions | 15        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0: 42 48 09 80 45 0A 80 F0  FF FF 7F F0 FF FF 7F 66  BH..E..........f
00C0: 64 6F 31 08 80 02 03 10  08 80 00 E1 00 62 01 80  do1..........b..
00D0: F0 FF FF 7F F0 FF FF 7F  6D 61 69 6E 08 80 1C 0B  ........main....
00E0: 80 1C 0C 80 83 1E 17 AA  1E 17 1E 17 1E 17 1E 17  ................
00F0: 1E 17 1F 17 1E 17 1E 17  03 02 00 08 80 77 1F 17  .............w..
0100: 02 00 78 45 0D 80 F0 FF  FF 7F F0 FF FF 7F 77 68  ..xE..........wh
0110: 69 31 08 80 21 00                                 i1..!.          
```

#### Opcodes

```
  0: 0x00B0 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x00B1 [0x48] [System] [7340*]:
    → "The order has been given by your party leader to enter [Everbloom Hollow/the Ruhotz Silvermines/Ghoyu's Reverie]."
  2: 0x00B4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  3: 0x00C5 [0x02] IF !(Work_Zone[3] == 0*) GOTO 0x00E1
  4: 0x00CD [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
  5: 0x00DE [0x1C] WAIT(90* ticks)
  6: 0x00E1 [0x1C] WAIT(60* ticks)
  7: 0x00E4 [0x83] Work_Zone_1700[30] = GetGameTime()
  8: 0x00E7 [0xAA] VANA_DIEL_TIMESTAMP_CONVERTER(timestamp=Work_Zone_1700[30], year=Work_Zone_1700[30], month=Work_Zone_1700[30], day=Work_Zone_1700[30], weekday=Work_Zone_1700[30], hour=Work_Zone_1700[31], minute=Work_Zone_1700[30], moon=Work_Zone_1700[30])
  9: 0x00F8 [0x03] ExtData[1]->WorkLocal[2] = 0*
 10: 0x00FD [0x77] SET_EVENT_TIME_WEATHER(hour=Work_Zone_1700[31], weather=ExtData[1]->WorkLocal[2])
 11: 0x0102 [0x78] ENABLE_GAME_TIMER_RESET_WEATHER()
 12: 0x0103 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 13: 0x0114 [0x21] END_EVENT
 14: 0x0115 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0116   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                   1F 00  0E 80 0F 80 08 80 1F 01        ..........
0120: 00                                                .               
```

#### Opcodes

```
  0: 0x0116 [0x1F] MOVE_ENTITY: EventEntity moves to X=17.414*, Z=3.361*, Y=0.000*
  1: 0x011E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0120 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0121   |
| Data Size    | 38 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:    32 10 80 1F 00 11 80  12 80 13 80 1F 01 6F 1E   2............o.
0130: DF E0 08 01 6F 76 F0 FF  FF 7F 7B F0 FF FF 7F 27  ....ov....{....'
0140: 0F F0 FF FF 7F 04 00                              .......         
```

#### Opcodes

```
  0: 0x0121 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0124 [0x1F] MOVE_ENTITY: EventEntity moves to X=383.908*, Z=-1.726*, Y=10.999*
  2: 0x012C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x012E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x012F [0x1E] EventEntity looks at Zogbog (ID: 17359071/0x0108E0DF) and starts talking
  5: 0x0134 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0135 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until LocalPlayer Render.Flags0 and Render.Flags3 conditions are met
  7: 0x013A [0x7B] LocalPlayer stops talking
  8: 0x013F [0x27] REQ_SET(priority=0x0F, entity_id=LocalPlayer, tag_num=0x04)
  9: 0x0146 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0147   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                      32  10 80 1F 00 14 80 15 80         2........
0150: 16 80 1F 01 00                                    .....           
```

#### Opcodes

```
  0: 0x0147 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x014A [0x1F] MOVE_ENTITY: EventEntity moves to X=370.433*, Z=-3.540*, Y=10.159*
  2: 0x0152 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0154 [0x00] END_REQSTACK()
```
