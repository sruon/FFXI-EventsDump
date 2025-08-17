# 17743878 - Tiger Tooth

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Port Bastok (ID: 236) |
| Block Size       | 364 bytes             |
| Total Events     | 10                    |
| References Count | 24                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [1](#event-1)            | 0x0001       |     10 |              2 |
| [65535.1](#event-655351) | 0x000B       |     39 |              9 |
| [65535.2](#event-655352) | 0x0032       |      6 |              2 |
| [12](#event-12)          | 0x0038       |     78 |             14 |
| [1008](#event-1008)      | 0x0086       |      1 |              1 |
| [1009](#event-1009)      | 0x0087       |      1 |              1 |
| [1010](#event-1010)      | 0x0088       |      1 |              1 |
| [65535.3](#event-655353) | 0x0089       |     37 |              8 |
| [65535.4](#event-655354) | 0x00AE       |     37 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x206F3     |      132851 |
|       1 | 0xFFFFC502  |  4294952194 |
|       2 | 0x2133      |        8499 |
|       3 | 0x0A16      |        2582 |
|       4 | 0x000D      |          13 |
|       5 | 0x1F9C7     |      129479 |
|       6 | 0xFFFFDC21  |  4294958113 |
|       7 | 0x1F7F7     |      129015 |
|       8 | 0xFFFFDF51  |  4294958929 |
|       9 | 0x1FE67     |      130663 |
|      10 | 0xFFFFE777  |  4294961015 |
|      11 | 0x03AF      |         943 |
|      12 | 0x000F      |          15 |
|      13 | 0x003C      |          60 |
|      14 | 0x1D02      |        7426 |
|      15 | 0x0960      |        2400 |
|      16 | 0x1D03      |        7427 |
|      17 | 0x2180E     |      137230 |
|      18 | 0xFFFFF532  |  4294964530 |
|      19 | 0x0677      |        1655 |
|      20 | 0x0001      |           1 |
|      21 | 0x000A      |          10 |
|      22 | 0x20897     |      133271 |
|      23 | 0xFFFFEFF6  |  4294963190 |

## String References

- **7426**: The North Gate and Beligen Square are down these stairs. Cross the drawbridge from the square if you want to get to the residential area.
- **7427**: Go straight west and you'll come across a goods store and the tavern. Further west is the road leading to the Markets District.

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

### Event 1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    37 00 80 01 80 02 80  03 80 00                  7.........     
```

#### Opcodes

```
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=132.851*, z=-15.102*, y=8.499*, direction=226.9°*
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000B   |
| Data Size    | 39 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   32 04 80 1F 00             2....
0010: 05 80 06 80 02 80 1F 01  1F 00 07 80 08 80 02 80  ................
0020: 1F 01 1F 00 09 80 0A 80  02 80 1F 01 1E 04 C0 0E  ................
0030: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x000B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x000E [0x1F] MOVE_ENTITY: EventEntity moves to X=129.479*, Z=-9.183*, Y=8.499*
  2: 0x0016 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0018 [0x1F] MOVE_ENTITY: EventEntity moves to X=129.015*, Z=-8.367*, Y=8.499*
  4: 0x0020 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0022 [0x1F] MOVE_ENTITY: EventEntity moves to X=130.663*, Z=-6.281*, Y=8.499*
  6: 0x002A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x002C [0x1E] EventEntity looks at Cornelia (ID: 17743876/0x010EC004) and starts talking
  8: 0x0031 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0032  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:       5E 69 64 6C 30 00                             ^idl0.        
```

#### Opcodes

```
  0: 0x0032 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0037 [0x00] END_REQSTACK()
```

### Event 12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0038   |
| Data Size    | 78 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                          39 0B 80 1C 0C 80 66 0D          9.....f.
0040: 80 06 C0 0E 01 06 C0 0E  01 70 6F 69 30 1D 0E 80  .........poi0...
0050: 23 53 06 C0 0E 01 06 C0  0E 01 70 6F 69 30 39 0F  #S........poi09.
0060: 80 1C 0C 80 66 0D 80 06  C0 0E 01 06 C0 0E 01 70  ....f..........p
0070: 6F 69 30 1D 10 80 23 53  06 C0 0E 01 06 C0 0E 01  oi0...#S........
0080: 70 6F 69 30 21 00                                 poi0!.          
```

#### Opcodes

```
  0: 0x0038 [0x39] SET_ENTITY_DIRECTION(direction=5.2°*)
  1: 0x003B [0x1C] WAIT(15* ticks)
  2: 0x003E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "poi0" with entities [Tiger Tooth (ID: 17743878/0x010EC006), Tiger Tooth (ID: 17743878/0x010EC006)], work=60*
  3: 0x004D [0x1D] PRINT_EVENT_MESSAGE(message_id=7426*)
    → "The North Gate and Beligen Square are down these stairs. Cross the drawbridge from the square if you want to get to the residential area."
  4: 0x0050 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0051 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi0" with entities [Tiger Tooth (ID: 17743878/0x010EC006), Tiger Tooth (ID: 17743878/0x010EC006)]
  6: 0x005E [0x39] SET_ENTITY_DIRECTION(direction=13.2°*)
  7: 0x0061 [0x1C] WAIT(15* ticks)
  8: 0x0064 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "poi0" with entities [Tiger Tooth (ID: 17743878/0x010EC006), Tiger Tooth (ID: 17743878/0x010EC006)], work=60*
  9: 0x0073 [0x1D] PRINT_EVENT_MESSAGE(message_id=7427*)
    → "Go straight west and you'll come across a goods store and the tavern. Further west is the road leading to the Markets District."
 10: 0x0076 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0077 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi0" with entities [Tiger Tooth (ID: 17743878/0x010EC006), Tiger Tooth (ID: 17743878/0x010EC006)]
 12: 0x0084 [0x21] END_EVENT
 13: 0x0085 [0x00] END_REQSTACK()
```

### Event 1008

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0086  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                   00                                    .         
```

#### Opcodes

```
  0: 0x0086 [0x00] END_REQSTACK()
```

### Event 1009

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0087  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                      00                                  .        
```

#### Opcodes

```
  0: 0x0087 [0x00] END_REQSTACK()
```

### Event 1010

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0088  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                          00                               .       
```

#### Opcodes

```
  0: 0x0088 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0089   |
| Data Size    | 37 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                             37 11 80 12 80 02 80           7......
0090: 13 80 1C 14 80 32 15 80  1F 00 16 80 17 80 02 80  .....2..........
00A0: 1F 01 6F 79 00 F8 FF FF  7F 82 C0 0E 01 00        ..oy..........  
```

#### Opcodes

```
  0: 0x0089 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=137.230*, z=-2.766*, y=8.499*, direction=145.5°*
  1: 0x0092 [0x1C] WAIT(1* ticks)
  2: 0x0095 [0x32] ExtData[1]->MainSpeed = 10* * 0.1
  3: 0x0098 [0x1F] MOVE_ENTITY: EventEntity moves to X=133.271*, Z=-4.106*, Y=8.499*
  4: 0x00A0 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x00A2 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x00A3 [0x79] EventEntity looks at Cid (ID: 17744002/0x010EC082) (Basic look)
  7: 0x00AD [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AE   |
| Data Size    | 37 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                            37 11                7.
00B0: 80 12 80 02 80 13 80 1C  14 80 32 15 80 1F 00 16  ..........2.....
00C0: 80 17 80 02 80 1F 01 6F  79 00 F8 FF FF 7F 83 C0  .......oy.......
00D0: 0E 01 00                                          ...             
```

#### Opcodes

```
  0: 0x00AE [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=137.230*, z=-2.766*, y=8.499*, direction=145.5°*
  1: 0x00B7 [0x1C] WAIT(1* ticks)
  2: 0x00BA [0x32] ExtData[1]->MainSpeed = 10* * 0.1
  3: 0x00BD [0x1F] MOVE_ENTITY: EventEntity moves to X=133.271*, Z=-4.106*, Y=8.499*
  4: 0x00C5 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x00C7 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x00C8 [0x79] EventEntity looks at Ayame (ID: 17744003/0x010EC083) (Basic look)
  7: 0x00D2 [0x00] END_REQSTACK()
```
