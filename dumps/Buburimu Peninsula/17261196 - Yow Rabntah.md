# 17261196 - Yow Rabntah

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Buburimu Peninsula (ID: 118) |
| Block Size       | 228 bytes                    |
| Total Events     | 14                           |
| References Count | 20                           |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [21](#event-21)            | 0x0001       |      1 |              1 |
| [22](#event-22)            | 0x0002       |      1 |              1 |
| [64](#event-64)            | 0x0003       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0004       |     15 |              4 |
| [65535.2](#event-655352)   | 0x0013       |     10 |              2 |
| [65535.3](#event-655353)   | 0x001D       |      1 |              1 |
| [65535.4](#event-655354)   | 0x001E       |      1 |              1 |
| [65535.5](#event-655355)   | 0x001F       |      1 |              1 |
| [65535.6](#event-655356)   | 0x0020       |      1 |              1 |
| [65535.7](#event-655357)   | 0x0021       |     10 |              2 |
| [65535.8](#event-655358)   | 0x002B       |     10 |              2 |
| [65535.9](#event-655359)   | 0x0035       |     10 |              2 |
| [65535.10](#event-6553510) | 0x003F       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xBD51      |       48465 |
|       1 | 0xFFFEE945  |  4294895941 |
|       2 | 0x2713      |       10003 |
|       3 | 0x0359      |         857 |
|       4 | 0x88EDE     |      560862 |
|       5 | 0xFFFBB8AD  |  4294686893 |
|       6 | 0x0000      |           0 |
|       7 | 0x0C36      |        3126 |
|       8 | 0x83BC      |       33724 |
|       9 | 0xFFFF3741  |  4294915905 |
|      10 | 0x232B      |        9003 |
|      11 | 0x0DB6      |        3510 |
|      12 | 0xFFFA848C  |  4294608012 |
|      13 | 0x4426      |       17446 |
|      14 | 0xFFFF76C9  |  4294932169 |
|      15 | 0x0941      |        2369 |
|      16 | 0xFFF9C879  |  4294559865 |
|      17 | 0x44DB      |       17627 |
|      18 | 0xFFFF56CA  |  4294923978 |
|      19 | 0x0912      |        2322 |

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

### Event 21

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

### Event 22

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       00                                            .             
```

#### Opcodes

```
  0: 0x0002 [0x00] END_REQSTACK()
```

### Event 64

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0003  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          00                                          .            
```

#### Opcodes

```
  0: 0x0003 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0004   |
| Data Size    | 15 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             22 00 2F 00  F8 FF FF 7F 92 01 8C 62      "./........b
0010: 07 01 00                                          ...             
```

#### Opcodes

```
  0: 0x0004 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0006 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x000C [0x92] Yow Rabntah (ID: 17261196/0x0107628C)->Render.Flags3 ^= 0x01
  3: 0x0012 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0013   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:          37 00 80 01 80  02 80 03 80 00              7.........   
```

#### Opcodes

```
  0: 0x0013 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=48.465*, z=-71.355*, y=10.003*, direction=75.3°*
  1: 0x001C [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         00                     .  
```

#### Opcodes

```
  0: 0x001D [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            00                   . 
```

#### Opcodes

```
  0: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               00                 .
```

#### Opcodes

```
  0: 0x001F [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0020  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x0020 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0021   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    37 04 80 05 80 06 80  07 80 00                  7.........     
```

#### Opcodes

```
  0: 0x0021 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=560.862*, z=-280.403*, y=0.000*, direction=274.7°*
  1: 0x002A [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002B   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   37 08 80 09 80             7....
0030: 0A 80 0B 80 00                                    .....           
```

#### Opcodes

```
  0: 0x002B [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=33.724*, z=-51.391*, y=9.003*, direction=308.5°*
  1: 0x0034 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0035   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                37 0C 80  0D 80 0E 80 0F 80 00          7......... 
```

#### Opcodes

```
  0: 0x0035 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-359.284*, z=17.446*, y=-35.127*, direction=208.2°*
  1: 0x003E [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003F   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                               37                 7
0040: 10 80 11 80 12 80 13 80  00                       .........       
```

#### Opcodes

```
  0: 0x003F [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-407.431*, z=17.627*, y=-43.318*, direction=204.1°*
  1: 0x0048 [0x00] END_REQSTACK()
```
