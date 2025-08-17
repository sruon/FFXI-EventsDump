# 17350956 - Fodderchief Vokdek

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Ghelsba Outpost (ID: 140) |
| Block Size       | 92 bytes                  |
| Total Events     | 4                         |
| References Count | 8                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      3 |              2 |
| [32000](#event-32000)    | 0x0003       |     10 |              2 |
| [32001](#event-32001)    | 0x000D       |     10 |              2 |
| [65535.1](#event-655351) | 0x0017       |      3 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFDB7B0  |  4294817712 |
|       1 | 0x14F06     |       85766 |
|       2 | 0xFFFFC4B1  |  4294952113 |
|       3 | 0x06C0      |        1728 |
|       4 | 0xFFFD2221  |  4294779425 |
|       5 | 0xD15C      |       53596 |
|       6 | 0xFFFFD73B  |  4294956859 |
|       7 | 0x0658      |        1624 |

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 22 01 00                                          "..             
```

#### Opcodes

```
  0: 0x0000 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0002 [0x00] END_REQSTACK()
```

### Event 32000

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0003   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          37 00 80 01 80  02 80 03 80 00              7.........   
```

#### Opcodes

```
  0: 0x0003 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-149.584*, z=85.766*, y=-15.183*, direction=151.9°*
  1: 0x000C [0x00] END_REQSTACK()
```

### Event 32001

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000D   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         37 04 80               7..
0010: 05 80 06 80 07 80 00                              .......         
```

#### Opcodes

```
  0: 0x000D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-187.871*, z=53.596*, y=-10.437*, direction=142.7°*
  1: 0x0016 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0017  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      22  00 00                           "..      
```

#### Opcodes

```
  0: 0x0017 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0019 [0x00] END_REQSTACK()
```
