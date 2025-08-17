# 17212077 - Gambilox Wanderling

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | North Gustaberg (ID: 106) |
| Block Size       | 128 bytes                 |
| Total Events     | 4                         |
| References Count | 11                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [200](#event-200)     | 0x0001       |      1 |              1 |
| [210](#event-210)     | 0x0002       |     29 |              6 |
| [211](#event-211)     | 0x001F       |     19 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFC9151  |  4294742353 |
|       2 | 0x6B994     |      440724 |
|       3 | 0x181FF     |       98815 |
|       4 | 0x0789      |        1929 |
|       5 | 0xFFFC7F45  |  4294737733 |
|       6 | 0x6C0AA     |      442538 |
|       7 | 0x183B0     |       99248 |
|       8 | 0xFFFC7C08  |  4294736904 |
|       9 | 0x6C120     |      442656 |
|      10 | 0x183A1     |       99233 |

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

### Event 210

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 29 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       4E 00 AD A2 06 01  32 00 80 37 01 80 02 80    N.....2..7....
0010: 03 80 04 80 1F 00 05 80  06 80 07 80 1F 01 00     ............... 
```

#### Opcodes

```
  0: 0x0002 [0x4E] SET_ENTITY_HIDE_FLAG: Show Gambilox Wanderling (ID: 17212077/0x0106A2AD)
  1: 0x0008 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x000B [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-224.943*, z=440.724*, y=98.815*, direction=169.5°*
  3: 0x0014 [0x1F] MOVE_ENTITY: EventEntity moves to X=-229.563*, Z=442.538*, Y=99.248*
  4: 0x001C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x001E [0x00] END_REQSTACK()
```

### Event 211

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               32                 2
0020: 00 80 1F 00 08 80 09 80  0A 80 1F 01 1E F0 FF FF  ................
0030: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x001F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0022 [0x1F] MOVE_ENTITY: EventEntity moves to X=-230.392*, Z=442.656*, Y=99.233*
  2: 0x002A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002C [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x0031 [0x00] END_REQSTACK()
```
