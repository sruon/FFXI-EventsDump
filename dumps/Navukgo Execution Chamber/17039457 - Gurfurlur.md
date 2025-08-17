# 17039457 - Gurfurlur

## Common Data

| Field            | Value                              |
|------------------|------------------------------------|
| Zone             | Navukgo Execution Chamber (ID: 64) |
| Block Size       | 136 bytes                          |
| Total Events     | 7                                  |
| References Count | 11                                 |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [1](#event-1)            | 0x0001       |      1 |              1 |
| [2](#event-2)            | 0x0002       |      1 |              1 |
| [65535.1](#event-655351) | 0x0003       |      9 |              3 |
| [65535.2](#event-655352) | 0x000C       |     10 |              2 |
| [65535.3](#event-655353) | 0x0016       |     10 |              2 |
| [65535.4](#event-655354) | 0x0020       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x5C40F     |      377871 |
|       1 | 0x5DF39     |      384825 |
|       2 | 0xFFFE3AE0  |  4294851296 |
|       3 | 0x0419      |        1049 |
|       4 | 0x5FD25     |      392485 |
|       5 | 0x5CBA8     |      379816 |
|       6 | 0xFFFE3887  |  4294850695 |
|       7 | 0x07F7      |        2039 |
|       8 | 0x000D      |          13 |
|       9 | 0x5F88A     |      391306 |
|      10 | 0x5EC7D     |      388221 |

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

### Event 2

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

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0003  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          22 00 2F 00 F8  FF FF 7F 00                 "./......    
```

#### Opcodes

```
  0: 0x0003 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0005 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x000B [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000C   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      37 00 80 01              7...
0010: 80 02 80 03 80 00                                 ......          
```

#### Opcodes

```
  0: 0x000C [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=377.871*, z=384.825*, y=-116.000*, direction=92.2°*
  1: 0x0015 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0016   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                   37 04  80 05 80 06 80 07 80 00        7.........
```

#### Opcodes

```
  0: 0x0016 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=392.485*, z=379.816*, y=-116.601*, direction=179.2°*
  1: 0x001F [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0020   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020: 32 08 80 1F 00 09 80 0A  80 02 80 1F 01 00        2.............  
```

#### Opcodes

```
  0: 0x0020 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0023 [0x1F] MOVE_ENTITY: EventEntity moves to X=391.306*, Z=388.221*, Y=-116.000*
  2: 0x002B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002D [0x00] END_REQSTACK()
```
