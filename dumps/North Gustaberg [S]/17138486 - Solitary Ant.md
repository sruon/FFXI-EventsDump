# 17138486 - Solitary Ant

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | North Gustaberg [S] (ID: 88) |
| Block Size       | 244 bytes                    |
| Total Events     | 9                            |
| References Count | 14                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [1](#event-1)            | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     22 |              6 |
| [65535.2](#event-655352) | 0x0018       |     14 |              4 |
| [2](#event-2)            | 0x0026       |     14 |              6 |
| [112](#event-112)        | 0x0034       |     14 |              6 |
| [7](#event-7)            | 0x0042       |     34 |              8 |
| [8](#event-8)            | 0x0064       |     35 |              9 |
| [204](#event-204)        | 0x0087       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x5C602     |      378370 |
|       2 | 0x2709D     |      159901 |
|       3 | 0x095D      |        2397 |
|       4 | 0x001E      |          30 |
|       5 | 0x5C38A     |      377738 |
|       6 | 0x259B5     |      154037 |
|       7 | 0x058F      |        1423 |
|       8 | 0x1F04      |        7940 |
|       9 | 0x1F1C      |        7964 |
|      10 | 0x0045      |          69 |
|      11 | 0x03DC      |         988 |
|      12 | 0x1F43      |        8003 |
|      13 | 0x1F42      |        8002 |

## String References

- **7940**: That wound was deep and recent. The turtlebacks have grown bold to attack a soldier so close to the city...!
- **7964**: The Bastok Markets lie on the other side of this gate.
- **8002**: Huh? Lost your $3, you say? We're in the middle of a crisis, so get your act together, soldier! Take this spare here, and be on your way!
- **8003**: You have $6, I see. The others are waiting for you at the Ruhotz Silvermines here in North Gustaberg. Don't make them wait.

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
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1F 00 01  80 02 80 03 80 1F 01 1E    2.............
0010: 37 83 05 01 1C 04 80 00                           7.......        
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=378.370*, Z=159.901*, Y=2.397*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x1E] EventEntity looks at Wolfram (ID: 17138487/0x01058337) and starts talking
  4: 0x0014 [0x1C] WAIT(30* ticks)
  5: 0x0017 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0018   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                          32 00 80 1F 00 05 80 06          2.......
0020: 80 07 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x0018 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x001B [0x1F] MOVE_ENTITY: EventEntity moves to X=377.738*, Z=154.037*, Y=1.423*
  2: 0x0023 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0025 [0x00] END_REQSTACK()
```

### Event 2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0026   |
| Data Size    | 14 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   1E F0  FF FF 7F 1C 04 80 1D 08        ..........
0030: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x0026 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x002B [0x1C] WAIT(30* ticks)
  2: 0x002E [0x1D] PRINT_EVENT_MESSAGE(message_id=7940*)
    → "That wound was deep and recent. The turtlebacks have grown bold to attack a soldier so close to the city...!"
  3: 0x0031 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0032 [0x21] END_EVENT
  5: 0x0033 [0x00] END_REQSTACK()
```

### Event 112

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0034   |
| Data Size    | 14 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:             1E F0 FF FF  7F 1C 04 80 1D 09 80 23      ...........#
0040: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0034 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0039 [0x1C] WAIT(30* ticks)
  2: 0x003C [0x1D] PRINT_EVENT_MESSAGE(message_id=7964*)
    → "The Bastok Markets lie on the other side of this gate."
  3: 0x003F [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0040 [0x21] END_EVENT
  5: 0x0041 [0x00] END_REQSTACK()
```

### Event 7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0042   |
| Data Size    | 34 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:       1E F0 FF FF 7F 1C  04 80 66 0A 80 F8 FF FF    ........f.....
0050: 7F F8 FF FF 7F 74 6C 6B  30 03 02 10 0B 80 1D 0C  .....tlk0.......
0060: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x0042 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0047 [0x1C] WAIT(30* ticks)
  2: 0x004A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=69*
  3: 0x0059 [0x03] Work_Zone[2] = 988*
  4: 0x005E [0x1D] PRINT_EVENT_MESSAGE(message_id=8003*)
    → "You have $6, I see. The others are waiting for you at the Ruhotz Silvermines here in North Gustaberg. Don't make them wait."
  5: 0x0061 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0062 [0x21] END_EVENT
  7: 0x0063 [0x00] END_REQSTACK()
```

### Event 8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0064   |
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:             42 1E F0 FF  FF 7F 1C 04 80 66 0A 80      B........f..
0070: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 03 02 10 0B  ........tlk0....
0080: 80 1D 0D 80 23 21 00                              ....#!.         
```

#### Opcodes

```
  0: 0x0064 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0065 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x006A [0x1C] WAIT(30* ticks)
  3: 0x006D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=69*
  4: 0x007C [0x03] Work_Zone[2] = 988*
  5: 0x0081 [0x1D] PRINT_EVENT_MESSAGE(message_id=8002*)
    → "Huh? Lost your $3, you say? We're in the middle of a crisis, so get your act together, soldier! Take this spare here, and be on your way!"
  6: 0x0084 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0085 [0x21] END_EVENT
  8: 0x0086 [0x00] END_REQSTACK()
```

### Event 204

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
