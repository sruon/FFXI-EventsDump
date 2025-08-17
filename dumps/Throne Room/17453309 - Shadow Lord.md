# 17453309 - Shadow Lord

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Throne Room (ID: 165) |
| Block Size       | 296 bytes             |
| Total Events     | 11                    |
| References Count | 27                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [32000](#event-32000)    | 0x0001       |      9 |              3 |
| [32004](#event-32004)    | 0x000A       |     16 |              3 |
| [65535.1](#event-655351) | 0x001A       |     10 |              2 |
| [65535.2](#event-655352) | 0x0024       |     10 |              2 |
| [65535.3](#event-655353) | 0x002E       |     10 |              2 |
| [65535.4](#event-655354) | 0x0038       |     15 |              5 |
| [65535.5](#event-655355) | 0x0047       |     10 |              2 |
| [65535.6](#event-655356) | 0x0051       |     10 |              2 |
| [65535.7](#event-655357) | 0x005B       |     10 |              2 |
| [6](#event-6)            | 0x0065       |     27 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFF8F031  |  4294504497 |
|       1 | 0xFFFC56BA  |  4294727354 |
|       2 | 0xFFFD72E1  |  4294800097 |
|       3 | 0x0FF9      |        4089 |
|       4 | 0xFFF85B14  |  4294466324 |
|       5 | 0xFFFC5671  |  4294727281 |
|       6 | 0xFFFD59E0  |  4294793696 |
|       7 | 0x0FC2      |        4034 |
|       8 | 0xFFF88C44  |  4294478916 |
|       9 | 0xFFFC56A4  |  4294727332 |
|      10 | 0xFFFD6020  |  4294795296 |
|      11 | 0x0FFF      |        4095 |
|      12 | 0xFFF881FE  |  4294476286 |
|      13 | 0x0014      |          20 |
|      14 | 0xFFF8A2F6  |  4294484726 |
|      15 | 0xFFF8DE21  |  4294499873 |
|      16 | 0xFFFC568F  |  4294727311 |
|      17 | 0xFFFD72D8  |  4294800088 |
|      18 | 0x0002      |           2 |
|      19 | 0x0000      |           0 |
|      20 | 0x0096      |         150 |
|      21 | 0x0080      |         128 |
|      22 | 0xFFF85710  |  4294465296 |
|      23 | 0xFFFC4CBC  |  4294724796 |
|      24 | 0xFFFD5850  |  4294793296 |
|      25 | 0x040B      |        1035 |
|      26 | 0x0001      |           1 |

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

### Event 32000

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    22 00 2F 00 F8 FF FF  7F 00                     "./......      
```

#### Opcodes

```
  0: 0x0001 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0003 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0009 [0x00] END_REQSTACK()
```

### Event 32004

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000A   |
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                2F 00 F8 FF FF 7F            /.....
0010: 37 00 80 01 80 02 80 03  80 00                    7.........      
```

#### Opcodes

```
  0: 0x000A [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  1: 0x0010 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-462.799*, z=-239.942*, y=-167.199*, direction=359.4°*
  2: 0x0019 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                37 04 80 05 80 06            7.....
0020: 80 07 80 00                                       ....            
```

#### Opcodes

```
  0: 0x001A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-500.972*, z=-240.015*, y=-173.600*, direction=354.5°*
  1: 0x0023 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0024   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             37 08 80 09  80 0A 80 0B 80 00            7.........  
```

#### Opcodes

```
  0: 0x0024 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-488.380*, z=-239.964*, y=-172.000*, direction=359.9°*
  1: 0x002D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002E   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            37 0C                7.
0030: 80 09 80 0A 80 0B 80 00                           ........        
```

#### Opcodes

```
  0: 0x002E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-491.010*, z=-239.964*, y=-172.000*, direction=359.9°*
  1: 0x0037 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0038   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                          32 0D 80 1F 00 0E 80 09          2.......
0040: 80 0A 80 1F 01 6F 00                              .....o.         
```

#### Opcodes

```
  0: 0x0038 [0x32] ExtData[1]->MainSpeed = 20* * 0.1
  1: 0x003B [0x1F] MOVE_ENTITY: EventEntity moves to X=-482.570*, Z=-239.964*, Y=-172.000*
  2: 0x0043 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0045 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0046 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0047   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      37  0F 80 10 80 11 80 12 80         7........
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x0047 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-467.423*, z=-239.985*, y=-167.208*, direction=0.2°*
  1: 0x0050 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0051   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:    6C F8 FF FF 7F 13 80  14 80 00                  l.........     
```

#### Opcodes

```
  0: 0x0051 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=150*)
  1: 0x005A [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005B   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   6C F8 FF FF 7F             l....
0060: 15 80 14 80 00                                    .....           
```

#### Opcodes

```
  0: 0x005B [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=150*)
  1: 0x0064 [0x00] END_REQSTACK()
```

### Event 6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0065   |
| Data Size    | 27 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                22 00 2F  00 F8 FF FF 7F 37 16 80       "./.....7..
0070: 17 80 18 80 19 80 6C F8  FF FF 7F 13 80 1A 80 00  ......l.........
```

#### Opcodes

```
  0: 0x0065 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0067 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x006D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-502.000*, z=-242.500*, y=-174.000*, direction=91.0°*
  3: 0x0076 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  4: 0x007F [0x00] END_REQSTACK()
```
