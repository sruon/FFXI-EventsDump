# 17772767 - Atori-Tutori

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Ru'Lude Gardens (ID: 243) |
| Block Size       | 640 bytes                 |
| Total Events     | 22                        |
| References Count | 27                        |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [10192](#event-10192)      | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |     10 |              2 |
| [65535.2](#event-655352)   | 0x000C       |     10 |              2 |
| [65535.3](#event-655353)   | 0x0016       |     10 |              2 |
| [65535.4](#event-655354)   | 0x0020       |     10 |              2 |
| [65535.5](#event-655355)   | 0x002A       |     15 |              5 |
| [65535.6](#event-655356)   | 0x0039       |     28 |              6 |
| [65535.7](#event-655357)   | 0x0055       |     15 |              5 |
| [65535.8](#event-655358)   | 0x0064       |     15 |              5 |
| [65535.9](#event-655359)   | 0x0073       |     15 |              5 |
| [65535.10](#event-6553510) | 0x0082       |     42 |              6 |
| [65535.11](#event-6553511) | 0x00AC       |     37 |              5 |
| [65535.12](#event-6553512) | 0x00D1       |    185 |             37 |
| [65535.13](#event-6553513) | 0x018A       |     14 |              4 |
| [65535.14](#event-6553514) | 0x0198       |     14 |              4 |
| [10139](#event-10139)      | 0x01A6       |      1 |              1 |
| [10195](#event-10195)      | 0x01A7       |      1 |              1 |
| [10196](#event-10196)      | 0x01A8       |      1 |              1 |
| [10198](#event-10198)      | 0x01A9       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x15F1      |        5617 |
|       1 | 0x1CF92     |      118674 |
|       2 | 0x0C1C      |        3100 |
|       3 | 0x0000      |           0 |
|       4 | 0x1FFB      |        8187 |
|       5 | 0x1D131     |      119089 |
|       6 | 0x04CA      |        1226 |
|       7 | 0x1D1DF     |      119263 |
|       8 | 0x1D4C      |        7500 |
|       9 | 0x000B      |          11 |
|      10 | 0x0C15      |        3093 |
|      11 | 0x1CF95     |      118677 |
|      12 | 0x0C1D      |        3101 |
|      13 | 0x157C      |        5500 |
|      14 | 0x000A      |          10 |
|      15 | 0x0001      |           1 |
|      16 | 0x0005      |           5 |
|      17 | 0x0002      |           2 |
|      18 | 0x0009      |           9 |
|      19 | 0x0046      |          70 |
|      20 | 0x008C      |         140 |
|      21 | 0x00D2      |         210 |
|      22 | 0x000D      |          13 |
|      23 | 0x2036      |        8246 |
|      24 | 0x1CE95     |      118421 |
|      25 | 0x158A      |        5514 |
|      26 | 0x1CE85     |      118405 |

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

### Event 10192

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
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       37 00 80 01 80 02  80 03 80 00                7.........    
```

#### Opcodes

```
  0: 0x0002 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=5.617*, z=118.674*, y=3.100*, direction=0.0°*
  1: 0x000B [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000C   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      37 04 80 05              7...
0010: 80 02 80 03 80 00                                 ......          
```

#### Opcodes

```
  0: 0x000C [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=8.187*, z=119.089*, y=3.100*, direction=0.0°*
  1: 0x0015 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0016   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                   37 06  80 07 80 02 80 03 80 00        7.........
```

#### Opcodes

```
  0: 0x0016 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=1.226*, z=119.263*, y=3.100*, direction=0.0°*
  1: 0x001F [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0020   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020: 37 08 80 07 80 02 80 03  80 00                    7.........      
```

#### Opcodes

```
  0: 0x0020 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=7.500*, z=119.263*, y=3.100*, direction=0.0°*
  1: 0x0029 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002A   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                32 09 80 1F 00 04            2.....
0030: 80 05 80 02 80 1F 01 6F  00                       .......o.       
```

#### Opcodes

```
  0: 0x002A [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x002D [0x1F] MOVE_ENTITY: EventEntity moves to X=8.187*, Z=119.089*, Y=3.100*
  2: 0x0035 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0037 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0038 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0039   |
| Data Size    | 28 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             32 09 80 1F 00 0A 80           2......
0040: 0B 80 0C 80 1F 01 6F 2C  DF 30 0F 01 DF 30 0F 01  ......o,.0...0..
0050: 6B 65 73 75 00                                    kesu.           
```

#### Opcodes

```
  0: 0x0039 [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x003C [0x1F] MOVE_ENTITY: EventEntity moves to X=3.093*, Z=118.677*, Y=3.101*
  2: 0x0044 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0046 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0047 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "kesu" with entities [Atori-Tutori (ID: 17772767/0x010F30DF), Atori-Tutori (ID: 17772767/0x010F30DF)]
  5: 0x0054 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0055   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                32 09 80  1F 00 0D 80 07 80 02 80       2..........
0060: 1F 01 6F 00                                       ..o.            
```

#### Opcodes

```
  0: 0x0055 [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x0058 [0x1F] MOVE_ENTITY: EventEntity moves to X=5.500*, Z=119.263*, Y=3.100*
  2: 0x0060 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0062 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0063 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0064   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:             32 09 80 1F  00 08 80 07 80 02 80 1F      2...........
0070: 01 6F 00                                          .o.             
```

#### Opcodes

```
  0: 0x0064 [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x0067 [0x1F] MOVE_ENTITY: EventEntity moves to X=7.500*, Z=119.263*, Y=3.100*
  2: 0x006F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0071 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0072 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0073   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:          32 0E 80 1F 00  06 80 07 80 02 80 1F 01     2............
0080: 6F 00                                             o.              
```

#### Opcodes

```
  0: 0x0073 [0x32] ExtData[1]->MainSpeed = 10* * 0.1
  1: 0x0076 [0x1F] MOVE_ENTITY: EventEntity moves to X=1.226*, Z=119.263*, Y=3.100*
  2: 0x007E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0080 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0081 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0082   |
| Data Size    | 42 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:       03 00 00 07 7F 1A  1B 01 07 01 00 0F 80 66    .............f
0090: 01 00 F8 FF FF 7F F8 FF  FF 7F 70 61 73 30 53 F8  ..........pas0S.
00A0: FF FF 7F F8 FF FF 7F 70  61 73 30 00              .......pas0.    
```

#### Opcodes

```
  0: 0x0082 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x0087 [0x1A] CALL_SUBROUTINE(address=0x011B)
  2: 0x008A [0x07] ExtData[1]->WorkLocal[1] += 1*
  3: 0x008F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  4: 0x009E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
  5: 0x00AB [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AC   |
| Data Size    | 37 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                      03 00 00 07              ....
00B0: 7F 1A F6 00 66 01 00 F8  FF FF 7F F8 FF FF 7F 73  ....f..........s
00C0: 68 61 30 53 F8 FF FF 7F  F8 FF FF 7F 73 68 61 30  ha0S........sha0
00D0: 00                                                .               
```

#### Opcodes

```
  0: 0x00AC [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x00B1 [0x1A] CALL_SUBROUTINE(address=0x00F6)
  2: 0x00B4 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x00C3 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha0" with entities [EventEntity, EventEntity]
  4: 0x00D0 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00D1    |
| Data Size    | 185 bytes |
| Instructions | 13        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:    03 00 00 07 7F 1A F6  00 66 01 00 F8 FF FF 7F   ........f......
00E0: F8 FF FF 7F 73 68 61 31  53 F8 FF FF 7F F8 FF FF  ....sha1S.......
00F0: 7F 73 68 61 31 00 03 01  00 00 00 02 01 00 10 80  .sha1...........
0100: 05 0B 01 08 01 00 0F 80  01 10 01 08 01 00 11 80  ................
0110: 14 01 00 0E 80 07 01 00  12 80 1B 03 01 00 00 00  ................
0120: 02 01 00 10 80 05 30 01  08 01 00 0F 80 01 35 01  ......0.......5.
0130: 08 01 00 11 80 14 01 00  0E 80 07 01 00 13 80 1B  ................
0140: 03 01 00 00 00 02 01 00  10 80 05 55 01 08 01 00  ...........U....
0150: 0F 80 01 5A 01 08 01 00  11 80 14 01 00 0E 80 07  ...Z............
0160: 01 00 14 80 1B 03 01 00  00 00 02 01 00 10 80 05  ................
0170: 7A 01 08 01 00 0F 80 01  7F 01 08 01 00 11 80 14  z...............
0180: 01 00 0E 80 07 01 00 15  80 1B                    ..........      
```

#### Opcodes

```
  0: 0x00D1 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x00D6 [0x1A] CALL_SUBROUTINE(address=0x00F6)
  2: 0x00D9 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha1" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x00E8 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha1" with entities [EventEntity, EventEntity]
  4: 0x00F5 [0x00] END_REQSTACK()

SUBROUTINE_00F6:
  5: 0x00F6 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
  6: 0x00FB [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x010B
  7: 0x0103 [0x08] ExtData[1]->WorkLocal[1] -= 1*
  8: 0x0108 [0x01] GOTO 0x0110
  9: 0x010B [0x08] ExtData[1]->WorkLocal[1] -= 2*

SUBROUTINE_0110:
 10: 0x0110 [0x14] ExtData[1]->WorkLocal[1] *= 10*
 11: 0x0115 [0x07] ExtData[1]->WorkLocal[1] += 9*
 12: 0x011A [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x011B [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x0120 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x0130
     0x0128 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x012D [0x01] GOTO 0x0135
     0x0130 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x0135 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x013A [0x07] ExtData[1]->WorkLocal[1] += 70*
     0x013F [0x1B] RETURN
     0x0140 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x0145 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x0155
     0x014D [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x0152 [0x01] GOTO 0x015A
     0x0155 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x015A [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x015F [0x07] ExtData[1]->WorkLocal[1] += 140*
     0x0164 [0x1B] RETURN
     0x0165 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x016A [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x017A
     0x0172 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x0177 [0x01] GOTO 0x017F
     0x017A [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x017F [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x0184 [0x07] ExtData[1]->WorkLocal[1] += 210*
     0x0189 [0x1B] RETURN
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x018A   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                                32 16 80 1F 00 17            2.....
0190: 80 18 80 0C 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x018A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x018D [0x1F] MOVE_ENTITY: EventEntity moves to X=8.246*, Z=118.421*, Y=3.101*
  2: 0x0195 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0197 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0198   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                          32 16 80 1F 00 19 80 1A          2.......
01A0: 80 0C 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x0198 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x019B [0x1F] MOVE_ENTITY: EventEntity moves to X=5.514*, Z=118.405*, Y=3.101*
  2: 0x01A3 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x01A5 [0x00] END_REQSTACK()
```

### Event 10139

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01A6  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:                   00                                    .         
```

#### Opcodes

```
  0: 0x01A6 [0x00] END_REQSTACK()
```

### Event 10195

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01A7  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:                      00                                  .        
```

#### Opcodes

```
  0: 0x01A7 [0x00] END_REQSTACK()
```

### Event 10196

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01A8  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:                          00                               .       
```

#### Opcodes

```
  0: 0x01A8 [0x00] END_REQSTACK()
```

### Event 10198

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01A9  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:                             00                             .      
```

#### Opcodes

```
  0: 0x01A9 [0x00] END_REQSTACK()
```
