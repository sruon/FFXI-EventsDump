# 17347121 - Burning Circle

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Horlais Peak (ID: 139) |
| Block Size       | 72 bytes               |
| Total Events     | 4                      |
| References Count | 4                      |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [32003](#event-32003) | 0x0001       |      1 |              1 |
| [32000](#event-32000) | 0x0002       |     10 |              2 |
| [32001](#event-32001) | 0x000C       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFF9F4E0  |  4294571232 |
|       1 | 0xFFFF043E  |  4294902846 |
|       2 | 0x171DA     |       94682 |
|       3 | 0x0648      |        1608 |

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

### Event 32003

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

### Event 32000

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       37 00 80 01 80 02  80 03 80 00                7.........    
```

#### Opcodes

```
  0: 0x0002 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-396.064*, z=-64.450*, y=94.682*, direction=141.3°*
  1: 0x000B [0x00] END_REQSTACK()
```

### Event 32001

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
  0: 0x000C [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-396.064*, z=-64.450*, y=94.682*, direction=141.3°*
  1: 0x0015 [0x00] END_REQSTACK()
```
