# 16982367 - Rughadjeen

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Aht Urhgan Whitegate (ID: 50) |
| Block Size       | 200 bytes                     |
| Total Events     | 9                             |
| References Count | 16                            |

## List of Events

| Event ID                  | Entrypoint   |   Size |   Instructions |
|---------------------------|--------------|--------|----------------|
| [65535](#event-65535)     | 0x0000       |      1 |              1 |
| [825](#event-825)         | 0x0001       |      1 |              1 |
| [65535.1](#event-65535-1) | 0x0002       |     20 |              6 |
| [65535.2](#event-65535-2) | 0x0016       |     29 |              7 |
| [882](#event-882)         | 0x0033       |      1 |              1 |
| [65535.3](#event-65535-3) | 0x0034       |      7 |              3 |
| [65535.4](#event-65535-4) | 0x003B       |      7 |              3 |
| [65535.5](#event-65535-5) | 0x0042       |     15 |              5 |
| [65535.6](#event-65535-6) | 0x0051       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x14022     |       81954 |
|       2 | 0x51D4B     |      335179 |
|       3 | 0xFFFF91A7  |  4294939047 |
|       4 | 0x12A43     |       76355 |
|       5 | 0xFFFDF0EB  |  4294832363 |
|       6 | 0xFFFFE891  |  4294961297 |
|       7 | 0x02F2      |         754 |
|       8 | 0x000D      |          13 |
|       9 | 0x134EF     |       79087 |
|      10 | 0xFFFDEBBC  |  4294831036 |
|      11 | 0x0001      |           1 |
|      12 | 0x0000      |           0 |
|      13 | 0xFFFD586E  |  4294793326 |
|      14 | 0xFFFD06E2  |  4294772450 |
|      15 | 0x3D32      |       15666 |

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

### Event 825

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
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1F 00 01  80 02 80 03 80 1F 01 6F    2............o
0010: 1E 65 21 03 01 00                                 .e!...          
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=81.954*, Z=335.179*, Y=-28.249*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0010 [0x1E] EventEntity looks at Gadalar (ID: 16982373/0x01032165) and starts talking
  5: 0x0015 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0016   |
| Data Size    | 29 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                   37 04  80 05 80 06 80 07 80 32        7........2
0020: 08 80 1F 00 09 80 0A 80  06 80 1F 01 6F 1E 5D 21  ............o.]!
0030: 03 01 00                                          ...             
```

#### Opcodes

```
  0: 0x0016 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=76.355*, z=-134.933*, y=-5.999*, direction=66.3°*
  1: 0x001F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0022 [0x1F] MOVE_ENTITY: EventEntity moves to X=79.087*, Z=-136.260*, Y=-5.999*
  3: 0x002A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x002C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x002D [0x1E] EventEntity looks at Biyaada (ID: 16982365/0x0103215D) and starts talking
  6: 0x0032 [0x00] END_REQSTACK()
```

### Event 882

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0033  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:          00                                          .            
```

#### Opcodes

```
  0: 0x0033 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0034  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:             AB 03 AC 01  0B 80 00                     .......     
```

#### Opcodes

```
  0: 0x0034 [0xAB] EventEntity->Render.Flags0 ^= 0x20000 // Toggle bit 17
  1: 0x0036 [0xAC] EventEntity->StatusEvent = 1*
  2: 0x003A [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003B  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   AC 01 0C 80 AB             .....
0040: 04 00                                             ..              
```

#### Opcodes

```
  0: 0x003B [0xAC] EventEntity->StatusEvent = 0*
  1: 0x003F [0xAB] EventEntity->Render.Flags0 |= 0x40000 // Set bit 18
  2: 0x0041 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0042   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:       32 00 80 1F 00 0D  80 0E 80 0F 80 1F 01 6F    2............o
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x0042 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0045 [0x1F] MOVE_ENTITY: EventEntity moves to X=-173.970*, Z=-194.846*, Y=15.666*
  2: 0x004D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x004F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0050 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0051  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:    00                                              .              
```

#### Opcodes

```
  0: 0x0051 [0x00] END_REQSTACK()
```
