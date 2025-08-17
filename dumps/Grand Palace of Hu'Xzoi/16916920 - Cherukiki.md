# 16916920 - Cherukiki

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Grand Palace of Hu'Xzoi (ID: 34) |
| Block Size       | 196 bytes                        |
| Total Events     | 11                               |
| References Count | 10                               |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      7 |              2 |
| [0](#event-0)            | 0x0007       |      1 |              1 |
| [65535.1](#event-655351) | 0x0008       |     18 |              4 |
| [65535.2](#event-655352) | 0x001A       |     10 |              2 |
| [65535.3](#event-655353) | 0x0024       |      9 |              3 |
| [65535.4](#event-655354) | 0x002D       |      9 |              3 |
| [65535.5](#event-655355) | 0x0036       |     10 |              2 |
| [65535.6](#event-655356) | 0x0040       |     10 |              2 |
| [1](#event-1)            | 0x004A       |     10 |              2 |
| [4](#event-4)            | 0x0054       |      1 |              1 |
| [65535.7](#event-655357) | 0x0055       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0xFFFFB85E  |  4294948958 |
|       4 | 0xFFFBB024  |  4294684708 |
|       5 | 0x0A93      |        2707 |
|       6 | 0xFFFFBC2A  |  4294949930 |
|       7 | 0xFFFB6BCB  |  4294667211 |
|       8 | 0x0271      |         625 |
|       9 | 0x0BD3      |        3027 |

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
0040:                                37 03 80 04 80 00            7.....
0050: 80 05 80 00                                       ....            
```

#### Opcodes

```
  0: 0x004A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-18.338*, z=-282.588*, y=0.000*, direction=237.9°*
  1: 0x0053 [0x00] END_REQSTACK()
```

### Event 4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0054  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:             00                                        .           
```

#### Opcodes

```
  0: 0x0054 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0055   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                37 06 80  07 80 08 80 09 80 00          7......... 
```

#### Opcodes

```
  0: 0x0055 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-17.366*, z=-300.085*, y=0.625*, direction=266.0°*
  1: 0x005E [0x00] END_REQSTACK()
```
