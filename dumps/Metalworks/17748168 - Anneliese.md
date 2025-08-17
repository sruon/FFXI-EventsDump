# 17748168 - Anneliese

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Metalworks (ID: 237) |
| Block Size       | 136 bytes            |
| Total Events     | 7                    |
| References Count | 7                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [946](#event-946)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     22 |              6 |
| [65535.2](#event-655352) | 0x0018       |     14 |              4 |
| [948](#event-948)        | 0x0026       |      1 |              1 |
| [65535.3](#event-655353) | 0x0027       |     22 |              6 |
| [950](#event-950)        | 0x003D       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFFCDD8  |  4294954456 |
|       2 | 0xFFFF9FF4  |  4294942708 |
|       3 | 0xFFFFD8F0  |  4294957296 |
|       4 | 0x001E      |          30 |
|       5 | 0xFFFFCE1D  |  4294954525 |
|       6 | 0xFFFFADE0  |  4294946272 |

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

### Event 946

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
0010: C6 D0 0E 01 1C 04 80 00                           ........        
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=-12.840*, Z=-24.588*, Y=-10.000*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x1E] EventEntity looks at Leonhardt (ID: 17748166/0x010ED0C6) and starts talking
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
0020: 80 03 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x0018 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x001B [0x1F] MOVE_ENTITY: EventEntity moves to X=-12.771*, Z=-21.024*, Y=-10.000*
  2: 0x0023 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0025 [0x00] END_REQSTACK()
```

### Event 948

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0026  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   00                                    .         
```

#### Opcodes

```
  0: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0027   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      32  00 80 1F 00 01 80 02 80         2........
0030: 03 80 1F 01 1E F0 FF FF  7F 1C 04 80 00           .............   
```

#### Opcodes

```
  0: 0x0027 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x002A [0x1F] MOVE_ENTITY: EventEntity moves to X=-12.840*, Z=-24.588*, Y=-10.000*
  2: 0x0032 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0034 [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x0039 [0x1C] WAIT(30* ticks)
  5: 0x003C [0x00] END_REQSTACK()
```

### Event 950

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         00                     .  
```

#### Opcodes

```
  0: 0x003D [0x00] END_REQSTACK()
```
