# 17118025 - Five Moons

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Vunkerl Inlet [S] (ID: 83) |
| Block Size       | 224 bytes                  |
| Total Events     | 11                         |
| References Count | 15                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [114](#event-114)        | 0x0001       |      7 |              2 |
| [65535.1](#event-655351) | 0x0008       |     11 |              3 |
| [115](#event-115)        | 0x0013       |      7 |              2 |
| [65535.2](#event-655352) | 0x001A       |     11 |              3 |
| [65535.3](#event-655353) | 0x0025       |     19 |              5 |
| [116](#event-116)        | 0x0038       |      7 |              2 |
| [117](#event-117)        | 0x003F       |      7 |              2 |
| [65535.4](#event-655354) | 0x0046       |     10 |              2 |
| [65535.5](#event-655355) | 0x0050       |     10 |              2 |
| [65535.6](#event-655356) | 0x005A       |     11 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFA7BCD  |  4294605773 |
|       1 | 0x44168     |      278888 |
|       2 | 0xFFFF7F7E  |  4294934398 |
|       3 | 0xFFFD4D86  |  4294790534 |
|       4 | 0x2B4F6     |      177398 |
|       5 | 0x03D5      |         981 |
|       6 | 0xFFFDB276  |  4294816374 |
|       7 | 0x2C878     |      182392 |
|       8 | 0x066F      |        1647 |
|       9 | 0x0190      |         400 |
|      10 | 0x0080      |         128 |
|      11 | 0x001E      |          30 |
|      12 | 0x0000      |           0 |
|      13 | 0xFFFA34B7  |  4294587575 |
|      14 | 0x44482     |      279682 |

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

### Event 114

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0008   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          1F 00 00 80 01 80 02 80          ........
0010: 1F 01 00                                          ...             
```

#### Opcodes

```
  0: 0x0008 [0x1F] MOVE_ENTITY: EventEntity moves to X=-361.523*, Z=278.888*, Y=-32.898*
  1: 0x0010 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0012 [0x00] END_REQSTACK()
```

### Event 115

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0013  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:          92 01 F8 FF FF  7F 00                       .......      
```

#### Opcodes

```
  0: 0x0013 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0019 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                1F 00 03 80 04 80            ......
0020: 05 80 1F 01 00                                    .....           
```

#### Opcodes

```
  0: 0x001A [0x1F] MOVE_ENTITY: EventEntity moves to X=-176.762*, Z=177.398*, Y=0.981*
  1: 0x0022 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0024 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0025   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                1F 00 06  80 07 80 08 80 1F 01 6F       ..........o
0030: 4B 49 33 05 01 09 80 00                           KI3.....        
```

#### Opcodes

```
  0: 0x0025 [0x1F] MOVE_ENTITY: EventEntity moves to X=-150.922*, Z=182.392*, Y=1.647*
  1: 0x002D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x002F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0030 [0x4B] UPDATE_ENTITY_YAW(entity=Five Moons (ID: 17118025/0x01053349), yaw=2.2°*)
  4: 0x0037 [0x00] END_REQSTACK()
```

### Event 116

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0038  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                          92 01 F8 FF FF 7F 00             ....... 
```

#### Opcodes

```
  0: 0x0038 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x003E [0x00] END_REQSTACK()
```

### Event 117

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003F  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                               92                 .
0040: 01 F8 FF FF 7F 00                                 ......          
```

#### Opcodes

```
  0: 0x003F [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0045 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0046   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   6C F8  FF FF 7F 0A 80 0B 80 00        l.........
```

#### Opcodes

```
  0: 0x0046 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=30*)
  1: 0x004F [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0050   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050: 6C F8 FF FF 7F 0C 80 0B  80 00                    l.........      
```

#### Opcodes

```
  0: 0x0050 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=30*)
  1: 0x0059 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005A   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                1F 00 0D 80 0E 80            ......
0060: 02 80 1F 01 00                                    .....           
```

#### Opcodes

```
  0: 0x005A [0x1F] MOVE_ENTITY: EventEntity moves to X=-379.721*, Z=279.682*, Y=-32.898*
  1: 0x0062 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0064 [0x00] END_REQSTACK()
```
