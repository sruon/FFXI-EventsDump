# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Yuhtunga Jungle (ID: 123) |
| Block Size       | 992 bytes                 |
| Total Events     | 15                        |
| References Count | 41                        |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65534](#event-65534)      | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |     24 |              4 |
| [65535.2](#event-655352)   | 0x001A       |     24 |              4 |
| [65535.3](#event-655353)   | 0x0032       |      7 |              3 |
| [65535.4](#event-655354)   | 0x0039       |    155 |             35 |
| [65535.5](#event-655355)   | 0x00D4       |      6 |              2 |
| [65535.6](#event-655356)   | 0x00DA       |      6 |              2 |
| [65535.7](#event-655357)   | 0x00E0       |      6 |              2 |
| [65535.8](#event-655358)   | 0x00E6       |     10 |              2 |
| [65535.9](#event-655359)   | 0x00F0       |     14 |              4 |
| [65535.10](#event-6553510) | 0x00FE       |     10 |              2 |
| [65535.11](#event-6553511) | 0x0108       |     10 |              2 |
| [105](#event-105)          | 0x0112       |    105 |             19 |
| [208](#event-208)          | 0x017B       |    370 |             49 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0000      |           0 |
|       2 | 0x0005      |           5 |
|       3 | 0x0002      |           2 |
|       4 | 0x000A      |          10 |
|       5 | 0x0009      |           9 |
|       6 | 0x0046      |          70 |
|       7 | 0x008C      |         140 |
|       8 | 0x00D2      |         210 |
|       9 | 0x58967     |      362855 |
|      10 | 0x350D5     |      217301 |
|      11 | 0x0F9F      |        3999 |
|      12 | 0x0E23      |        3619 |
|      13 | 0x000D      |          13 |
|      14 | 0x59228     |      365096 |
|      15 | 0x35856     |      219222 |
|      16 | 0x107E      |        4222 |
|      17 | 0x0E7D      |        3709 |
|      18 | 0x78422     |      492578 |
|      19 | 0x49CD9     |      302297 |
|      20 | 0x5207      |       20999 |
|      21 | 0x0E1B      |        3611 |
|      22 | 0x0029      |          41 |
|      23 | 0x00C9      |         201 |
|      24 | 0x003C      |          60 |
|      25 | 0x001E      |          30 |
|      26 | 0x1E57      |        7767 |
|      27 | 0x0027      |          39 |
|      28 | 0x00C8      |         200 |
|      29 | 0x007B      |         123 |
|      30 | 0x0013      |          19 |
|      31 | 0x0090      |         144 |
|      32 | 0xFFFACE5E  |  4294626910 |
|      33 | 0xFFF8D23B  |  4294496827 |
|      34 | 0x3DA2      |       15778 |
|      35 | 0x03B5      |         949 |
|      36 | 0x1EAE      |        7854 |
|      37 | 0x1EAF      |        7855 |
|      38 | 0x1EB0      |        7856 |
|      39 | 0x1EB4      |        7860 |
|      40 | 0x1EB1      |        7857 |

## String References

- **7767**: You dig up a strange wooden casket!

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 24 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       03 00 00 07 7F 1A  40 00 66 01 00 F8 FF FF    ......@.f.....
0010: 7F F8 FF FF 7F 74 6C 6B  30 00                    .....tlk0.      
```

#### Opcodes

```
  0: 0x0002 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x0007 [0x1A] CALL_SUBROUTINE(address=0x0040)
  2: 0x000A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x0019 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 24 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                03 00 00 07 7F 1A            ......
0020: 40 00 66 01 00 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  @.f..........tlk
0030: 31 00                                             1.              
```

#### Opcodes

```
  0: 0x001A [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x001F [0x1A] CALL_SUBROUTINE(address=0x0040)
  2: 0x0022 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x0031 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0032  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:       AB 03 AC 01 00 80  00                         .......       
```

#### Opcodes

```
  0: 0x0032 [0xAB] EventEntity->Render.Flags0 ^= 0x20000 // Toggle bit 17
  1: 0x0034 [0xAC] EventEntity->StatusEvent = 1*
  2: 0x0038 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0039    |
| Data Size    | 155 bytes |
| Instructions | 3         |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             AC 01 01 80 AB 04 00           .......
0040: 03 01 00 00 00 02 01 00  02 80 05 55 00 08 01 00  ...........U....
0050: 00 80 01 5A 00 08 01 00  03 80 14 01 00 04 80 07  ...Z............
0060: 01 00 05 80 1B 03 01 00  00 00 02 01 00 02 80 05  ................
0070: 7A 00 08 01 00 00 80 01  7F 00 08 01 00 03 80 14  z...............
0080: 01 00 04 80 07 01 00 06  80 1B 03 01 00 00 00 02  ................
0090: 01 00 02 80 05 9F 00 08  01 00 00 80 01 A4 00 08  ................
00A0: 01 00 03 80 14 01 00 04  80 07 01 00 07 80 1B 03  ................
00B0: 01 00 00 00 02 01 00 02  80 05 C4 00 08 01 00 00  ................
00C0: 80 01 C9 00 08 01 00 03  80 14 01 00 04 80 07 01  ................
00D0: 00 08 80 1B                                       ....            
```

#### Opcodes

```
  0: 0x0039 [0xAC] EventEntity->StatusEvent = 0*
  1: 0x003D [0xAB] EventEntity->Render.Flags0 |= 0x40000 // Set bit 18
  2: 0x003F [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0040 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x0045 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x0055
     0x004D [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x0052 [0x01] GOTO 0x005A
     0x0055 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x005A [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x005F [0x07] ExtData[1]->WorkLocal[1] += 9*
     0x0064 [0x1B] RETURN
     0x0065 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x006A [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x007A
     0x0072 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x0077 [0x01] GOTO 0x007F
     0x007A [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x007F [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x0084 [0x07] ExtData[1]->WorkLocal[1] += 70*
     0x0089 [0x1B] RETURN
     0x008A [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x008F [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x009F
     0x0097 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x009C [0x01] GOTO 0x00A4
     0x009F [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x00A4 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x00A9 [0x07] ExtData[1]->WorkLocal[1] += 140*
     0x00AE [0x1B] RETURN
     0x00AF [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x00B4 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x00C4
     0x00BC [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x00C1 [0x01] GOTO 0x00C9
     0x00C4 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x00C9 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x00CE [0x07] ExtData[1]->WorkLocal[1] += 210*
     0x00D3 [0x1B] RETURN
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00D4  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:             03 02 10 0B  7F 00                        ......      
```

#### Opcodes

```
  0: 0x00D4 [0x03] Work_Zone[2] = (Entity->Render.Flags01 >> 25) & 1
  1: 0x00D9 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00DA  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                03 09 10 07 7F 00            ......
```

#### Opcodes

```
  0: 0x00DA [0x03] Work_Zone[9] = Entity->Race
  1: 0x00DF [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00E0  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0: 03 02 10 06 7F 00                                 ......          
```

#### Opcodes

```
  0: 0x00E0 [0x03] Work_Zone[2] = Entity->JobId (if LocalPlayer)
  1: 0x00E5 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E6   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                   37 09  80 0A 80 0B 80 0C 80 00        7.........
```

#### Opcodes

```
  0: 0x00E6 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=362.855*, z=217.301*, y=3.999*, direction=318.1°*
  1: 0x00EF [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F0   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0: 32 0D 80 5A 00 0E 80 0F  80 10 80 5A 01 00        2..Z.......Z..  
```

#### Opcodes

```
  0: 0x00F0 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00F3 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=365.096*, Z=219.222*, Y=4.222*
  2: 0x00FB [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  3: 0x00FD [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FE   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                            37 0E                7.
0100: 80 0F 80 10 80 11 80 00                           ........        
```

#### Opcodes

```
  0: 0x00FE [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=365.096*, z=219.222*, y=4.222*, direction=326.0°*
  1: 0x0107 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0108   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                          37 12 80 13 80 14 80 15          7.......
0110: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0108 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=492.578*, z=302.297*, y=20.999*, direction=317.4°*
  1: 0x0111 [0x00] END_REQSTACK()
```

### Event 105

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0112    |
| Data Size    | 105 bytes |
| Instructions | 19        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:       20 01 42 6E F0 FF  FF 7F 16 80 99 F0 FF FF     .Bn..........
0120: 7F 45 17 80 F0 FF FF 7F  F0 FF FF 7F 77 68 6F 31  .E..........who1
0130: 01 80 1C 18 80 29 01 6A  B2 07 01 02 1C 19 80 45  .....).j.......E
0140: 17 80 F0 FF FF 7F F0 FF  FF 7F 77 68 69 31 01 80  ..........whi1..
0150: 48 1A 80 1C 18 80 6E F0  FF FF 7F 1B 80 99 F0 FF  H.....n.........
0160: FF 7F 29 01 6A B2 07 01  03 1C 1C 80 29 01 6A B2  ..).j.......).j.
0170: 07 01 04 A8 00 1D 80 01  80 21 00                 .........!.     
```

#### Opcodes

```
  0: 0x0112 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0114 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0115 [0x6E] LocalPlayer uses emote 41*
  3: 0x011C [0x99] Wait for LocalPlayer animation to complete
  4: 0x0121 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
  5: 0x0132 [0x1C] WAIT(60* ticks)
  6: 0x0135 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Casket (ID: 17281642/0x0107B26A), tag_num=0x02)
  7: 0x013C [0x1C] WAIT(30* ticks)
  8: 0x013F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
  9: 0x0150 [0x48] [System] [7767*]:
    → "You dig up a strange wooden casket!"
 10: 0x0153 [0x1C] WAIT(60* ticks)
 11: 0x0156 [0x6E] LocalPlayer uses emote 39*
 12: 0x015D [0x99] Wait for LocalPlayer animation to complete
 13: 0x0162 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Casket (ID: 17281642/0x0107B26A), tag_num=0x03)
 14: 0x0169 [0x1C] WAIT(200* ticks)
 15: 0x016C [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Casket (ID: 17281642/0x0107B26A), tag_num=0x04)
 16: 0x0173 [0xA8] MAP_MARKER_CONTROL: Reset/unlock markers (no map display), zone=123*, marker=0*
 17: 0x0179 [0x21] END_EVENT
 18: 0x017A [0x00] END_REQSTACK()
```

### Event 208

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x017B    |
| Data Size    | 370 bytes |
| Instructions | 49        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                                   42 46 01 03 02             BF...
0180: 00 05 10 45 1C 80 F8 FF  FF 7F F8 FF FF 7F 66 64  ...E..........fd
0190: 6F 30 01 80 55 1C 80 F8  FF FF 7F F8 FF FF 7F 66  o0..U..........f
01A0: 64 6F 30 4E 00 77 B2 07  01 4E 00 78 B2 07 01 38  do0N.w...N.x...8
01B0: 1E 80 79 00 F0 FF FF 7F  77 B2 07 01 03 05 10 02  ..y.....w.......
01C0: 10 03 06 10 02 10 03 07  10 02 10 15 05 10 1F 80  ................
01D0: 15 06 10 18 80 3F 07 10  07 10 18 80 37 20 80 21  .....?......7 .!
01E0: 80 22 80 23 80 45 02 80  F8 FF FF 7F F8 FF FF 7F  .".#.E..........
01F0: 73 30 30 36 01 80 4A 77  B2 07 01 F0 FF FF 7F 45  s006..Jw.......E
0200: 1C 80 F8 FF FF 7F F8 FF  FF 7F 66 64 69 31 01 80  ..........fdi1..
0210: 2B 77 B2 07 01 24 80 23  66 19 80 77 B2 07 01 77  +w...$.#f..w...w
0220: B2 07 01 74 6C 6B 30 2B  77 B2 07 01 25 80 23 02  ...tlk0+w...%.#.
0230: 04 10 01 80 01 81 02 66  19 80 77 B2 07 01 77 B2  .......f..w...w.
0240: 07 01 74 6C 6B 31 03 05  10 04 10 03 06 10 04 10  ..tlk1..........
0250: 03 07 10 04 10 15 05 10  1F 80 15 06 10 18 80 3F  ...............?
0260: 07 10 07 10 18 80 02 02  00 01 80 00 79 02 2B 77  ............y.+w
0270: B2 07 01 26 80 23 01 81  02 2B 77 B2 07 01 27 80  ...&.#...+w...'.
0280: 23 66 19 80 77 B2 07 01  77 B2 07 01 70 61 73 30  #f..w...w...pas0
0290: 2B 77 B2 07 01 28 80 23  52 02 80 F8 FF FF 7F F8  +w...(.#R.......
02A0: FF FF 7F 73 30 30 36 45  1C 80 F8 FF FF 7F F8 FF  ...s006E........
02B0: FF 7F 66 64 6F 31 01 80  55 1C 80 F8 FF FF 7F F8  ..fdo1..U.......
02C0: FF FF 7F 66 64 6F 31 46  00 45 17 80 F0 FF FF 7F  ...fdo1F.E......
02D0: F0 FF FF 7F 71 73 74 63  01 80 45 1C 80 F8 FF FF  ....qstc..E.....
02E0: 7F F8 FF FF 7F 66 64 69  32 01 80 21 00           .....fdi2..!.   
```

#### Opcodes

```
  0: 0x017B [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x017C [0x46] CAMERA_CONTROL: Disable user control
  2: 0x017E [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[5]
  3: 0x0183 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [EventEntity, EventEntity], work=[200*, 0*]
  4: 0x0194 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo0" with entities [EventEntity, EventEntity], work=200*
  5: 0x01A3 [0x4E] SET_ENTITY_HIDE_FLAG: Show Marilleune (ID: 17281655/0x0107B277)
  6: 0x01A9 [0x4E] SET_ENTITY_HIDE_FLAG: Show Unnamed NPC (ID: 17281656/0x0107B278)
  7: 0x01AF [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  8: 0x01B2 [0x79] LocalPlayer looks at Marilleune (ID: 17281655/0x0107B277) (Basic look)
  9: 0x01BC [0x03] Work_Zone[5] = Work_Zone[2]
 10: 0x01C1 [0x03] Work_Zone[6] = Work_Zone[2]
 11: 0x01C6 [0x03] Work_Zone[7] = Work_Zone[2]
 12: 0x01CB [0x15] Work_Zone[5] /= 144*
 13: 0x01D0 [0x15] Work_Zone[6] /= 60*
 14: 0x01D5 [0x3F] Work_Zone[7] = Work_Zone[7] % 60*
 15: 0x01DC [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-340.386*, z=-470.469*, y=15.778*, direction=83.4°*
 16: 0x01E5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s006" with entities [EventEntity, EventEntity], work=[5*, 0*]
 17: 0x01F6 [0x4A] Marilleune (ID: 17281655/0x0107B277) looks at LocalPlayer
 18: 0x01FF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 19: 0x0210 [0x2B] Marilleune (ID: 17281655/0x0107B277) [7854*]:
    → "You've helped our poor girl find her way home! I don't know how to thank you!"
 20: 0x0217 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x0218 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Marilleune (ID: 17281655/0x0107B277), Marilleune (ID: 17281655/0x0107B277)], work=30*
 22: 0x0227 [0x2B] Marilleune (ID: 17281655/0x0107B277) [7855*]:
    → "And to think you made it here in a mere $3 [hour/hours] ($4 [minute/minutes] and $5 [second/seconds] Earth time)!"
 23: 0x022E [0x23] WAIT_FOR_DIALOG_INTERACTION
 24: 0x022F [0x02] IF !(Work_Zone[4] == 0*) GOTO 0x0281
 25: 0x0237 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [Marilleune (ID: 17281655/0x0107B277), Marilleune (ID: 17281655/0x0107B277)], work=30*
 26: 0x0246 [0x03] Work_Zone[5] = Work_Zone[4]
 27: 0x024B [0x03] Work_Zone[6] = Work_Zone[4]
 28: 0x0250 [0x03] Work_Zone[7] = Work_Zone[4]
 29: 0x0255 [0x15] Work_Zone[5] /= 144*
 30: 0x025A [0x15] Work_Zone[6] /= 60*
 31: 0x025F [0x3F] Work_Zone[7] = Work_Zone[7] % 60*
 32: 0x0266 [0x02] IF !(ExtData[1]->WorkLocal[2] == 0*) GOTO 0x0279
 33: 0x026E [0x2B] Marilleune (ID: 17281655/0x0107B277) [7856*]:
    → "Oh, and by the way, the fastest adventurer to date has been %0. That talented rider traversed the same course as you in $3 [hour/hours] ($4 [minute/minutes] and $5 [second/seconds] Earth time)!"
 34: 0x0275 [0x23] WAIT_FOR_DIALOG_INTERACTION
 35: 0x0276 [0x01] GOTO 0x0281
 36: 0x0279 [0x2B] Marilleune (ID: 17281655/0x0107B277) [7860*]:
    → "Oh, and by the way, the fastest adventurer to date has been...you! Your remarkable record of $3 [hour/hours] ($4 [minute/minutes] and $5 [second/seconds] Earth time) still stands strong!"
 37: 0x0280 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0281:
 38: 0x0281 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [Marilleune (ID: 17281655/0x0107B277), Marilleune (ID: 17281655/0x0107B277)], work=30*
 39: 0x0290 [0x2B] Marilleune (ID: 17281655/0x0107B277) [7857*]:
    → "Anyway, please take this as a token of our appreciation. And stop by again sometime. We may have more work for you!"
 40: 0x0297 [0x23] WAIT_FOR_DIALOG_INTERACTION
 41: 0x0298 [0x52] END_LOAD_SCHEDULER: End scheduler "s006" with entities [EventEntity, EventEntity], work=5*
 42: 0x02A7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 43: 0x02B8 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [EventEntity, EventEntity], work=200*
 44: 0x02C7 [0x46] CAMERA_CONTROL: Restore default settings
 45: 0x02C9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 46: 0x02DA [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [EventEntity, EventEntity], work=[200*, 0*]
 47: 0x02EB [0x21] END_EVENT
 48: 0x02EC [0x00] END_REQSTACK()
```
