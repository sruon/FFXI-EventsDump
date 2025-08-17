# 17735800 - Francmage

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Bastok Mines (ID: 234) |
| Block Size       | 224 bytes              |
| Total Events     | 14                     |
| References Count | 19                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [200](#event-200)        | 0x0001       |      1 |              1 |
| [201](#event-201)        | 0x0002       |      1 |              1 |
| [597](#event-597)        | 0x0003       |      1 |              1 |
| [65535.1](#event-655351) | 0x0004       |     15 |              4 |
| [65535.2](#event-655352) | 0x0013       |     10 |              2 |
| [208](#event-208)        | 0x001D       |      1 |              1 |
| [213](#event-213)        | 0x001E       |      1 |              1 |
| [214](#event-214)        | 0x001F       |      1 |              1 |
| [219](#event-219)        | 0x0020       |      1 |              1 |
| [65535.3](#event-655353) | 0x0021       |     10 |              2 |
| [65535.4](#event-655354) | 0x002B       |     10 |              2 |
| [65535.5](#event-655355) | 0x0035       |     10 |              2 |
| [65535.6](#event-655356) | 0x003F       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x27436     |      160822 |
|       1 | 0x26D69     |      159081 |
|       2 | 0xFFFFF830  |  4294965296 |
|       3 | 0x0CB7      |        3255 |
|       4 | 0x885F0     |      558576 |
|       5 | 0xFFFBCEEB  |  4294692587 |
|       6 | 0xFFFFFFBF  |  4294967231 |
|       7 | 0x021B      |         539 |
|       8 | 0x2224B     |      139851 |
|       9 | 0x1D837     |      120887 |
|      10 | 0x070E      |        1806 |
|      11 | 0xFFFA8BFC  |  4294609916 |
|      12 | 0x43B2      |       17330 |
|      13 | 0xFFFF76C3  |  4294932163 |
|      14 | 0x0A02      |        2562 |
|      15 | 0xFFF9CCA4  |  4294560932 |
|      16 | 0x4C28      |       19496 |
|      17 | 0xFFFF5748  |  4294924104 |
|      18 | 0x07F4      |        2036 |

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

### Event 200

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

### Event 201

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

### Event 597

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
0000:             22 00 2F 00  F8 FF FF 7F 92 01 78 A0      "./.......x.
0010: 0E 01 00                                          ...             
```

#### Opcodes

```
  0: 0x0004 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0006 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x000C [0x92] Francmage (ID: 17735800/0x010EA078)->Render.Flags3 ^= 0x01
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
  0: 0x0013 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=160.822*, z=159.081*, y=-2.000*, direction=286.1°*
  1: 0x001C [0x00] END_REQSTACK()
```

### Event 208

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

### Event 213

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

### Event 214

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

### Event 219

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

### Event 65535.3

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
  0: 0x0021 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=558.576*, z=-274.709*, y=-0.065*, direction=47.4°*
  1: 0x002A [0x00] END_REQSTACK()
```

### Event 65535.4

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
0030: 02 80 0A 80 00                                    .....           
```

#### Opcodes

```
  0: 0x002B [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=139.851*, z=120.887*, y=-2.000*, direction=158.7°*
  1: 0x0034 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0035   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                37 0B 80  0C 80 0D 80 0E 80 00          7......... 
```

#### Opcodes

```
  0: 0x0035 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-357.380*, z=17.330*, y=-35.133*, direction=225.2°*
  1: 0x003E [0x00] END_REQSTACK()
```

### Event 65535.6

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
0040: 0F 80 10 80 11 80 12 80  00                       .........       
```

#### Opcodes

```
  0: 0x003F [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-406.364*, z=19.496*, y=-43.192*, direction=178.9°*
  1: 0x0048 [0x00] END_REQSTACK()
```
