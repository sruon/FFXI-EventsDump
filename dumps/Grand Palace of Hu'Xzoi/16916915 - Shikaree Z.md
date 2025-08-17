# 16916915 - Shikaree Z

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Grand Palace of Hu'Xzoi (ID: 34) |
| Block Size       | 292 bytes                        |
| Total Events     | 15                               |
| References Count | 21                               |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      7 |              2 |
| [0](#event-0)              | 0x0007       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0008       |     18 |              4 |
| [65535.2](#event-655352)   | 0x001A       |     10 |              2 |
| [65535.3](#event-655353)   | 0x0024       |      9 |              3 |
| [65535.4](#event-655354)   | 0x002D       |      9 |              3 |
| [65535.5](#event-655355)   | 0x0036       |     10 |              2 |
| [65535.6](#event-655356)   | 0x0040       |     10 |              2 |
| [1](#event-1)              | 0x004A       |     10 |              2 |
| [65535.7](#event-655357)   | 0x0054       |     15 |              5 |
| [2](#event-2)              | 0x0063       |      1 |              1 |
| [65535.8](#event-655358)   | 0x0064       |     10 |              2 |
| [65535.9](#event-655359)   | 0x006E       |     10 |              2 |
| [4](#event-4)              | 0x0078       |      1 |              1 |
| [65535.10](#event-6553510) | 0x0079       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0xFFFFAEC0  |  4294946496 |
|       4 | 0xFFFB94F7  |  4294677751 |
|       5 | 0x01C0      |         448 |
|       6 | 0x0C47      |        3143 |
|       7 | 0x000D      |          13 |
|       8 | 0xFFFFAFEC  |  4294946796 |
|       9 | 0xFFFBA248  |  4294681160 |
|      10 | 0xFFFFB33B  |  4294947643 |
|      11 | 0xFFFB0AB0  |  4294642352 |
|      12 | 0x0270      |         624 |
|      13 | 0x0F36      |        3894 |
|      14 | 0xFFFFE353  |  4294959955 |
|      15 | 0xFFFB1320  |  4294644512 |
|      16 | 0x01F3      |         499 |
|      17 | 0x0D97      |        3479 |
|      18 | 0xFFFFB05C  |  4294946908 |
|      19 | 0xFFFB772A  |  4294670122 |
|      20 | 0x0C1B      |        3099 |

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 92 01 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x0000 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0006 [0x00] END_REQSTACK()
```

### Event 0

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0007  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                      00                                  .        
```

#### Opcodes

```
  0: 0x0007 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0008   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          22 00 2F 00 F8 FF FF 7F          "./.....
0010: 6C F8 FF FF 7F 00 80 01  80 00                    l.........      
```

#### Opcodes

```
  0: 0x0008 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x000A [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0010 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x0019 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                6C F8 FF FF 7F 02            l.....
0020: 80 01 80 00                                       ....            
```

#### Opcodes

```
  0: 0x001A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0023 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0024  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             22 00 2F 00  F8 FF FF 7F 00               "./......   
```

#### Opcodes

```
  0: 0x0024 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0026 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x002C [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002D  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         22 01 2F               "./
0030: 01 F8 FF FF 7F 00                                 ......          
```

#### Opcodes

```
  0: 0x002D [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x002F [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x0035 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0036   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                   6C F8  FF FF 7F 00 80 01 80 00        l.........
```

#### Opcodes

```
  0: 0x0036 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x003F [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0040   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040: 6C F8 FF FF 7F 02 80 01  80 00                    l.........      
```

#### Opcodes

```
  0: 0x0040 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0049 [0x00] END_REQSTACK()
```

### Event 1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                37 03 80 04 80 05            7.....
0050: 80 06 80 00                                       ....            
```

#### Opcodes

```
  0: 0x004A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-20.800*, z=-289.545*, y=0.448*, direction=276.2°*
  1: 0x0053 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0054   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:             32 07 80 1F  00 08 80 09 80 00 80 1F      2...........
0060: 01 6F 00                                          .o.             
```

#### Opcodes

```
  0: 0x0054 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0057 [0x1F] MOVE_ENTITY: EventEntity moves to X=-20.500*, Z=-286.136*, Y=0.000*
  2: 0x005F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0061 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0062 [0x00] END_REQSTACK()
```

### Event 2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0063  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:          00                                          .            
```

#### Opcodes

```
  0: 0x0063 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0064   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:             37 0A 80 0B  80 0C 80 0D 80 00            7.........  
```

#### Opcodes

```
  0: 0x0064 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-19.653*, z=-324.944*, y=0.624*, direction=342.2°*
  1: 0x006D [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006E   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                            37 0E                7.
0070: 80 0F 80 10 80 11 80 00                           ........        
```

#### Opcodes

```
  0: 0x006E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-7.341*, z=-322.784*, y=0.499*, direction=305.8°*
  1: 0x0077 [0x00] END_REQSTACK()
```

### Event 4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0078  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                          00                               .       
```

#### Opcodes

```
  0: 0x0078 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0079   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                             37 12 80 13 80 0C 80           7......
0080: 14 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0079 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-20.388*, z=-297.174*, y=0.624*, direction=272.4°*
  1: 0x0082 [0x00] END_REQSTACK()
```
