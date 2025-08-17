# 17809548 - Atori-Tutori

## Common Data

| Field            | Value          |
|------------------|----------------|
| Zone             | Norg (ID: 252) |
| Block Size       | 104 bytes      |
| Total Events     | 4              |
| References Count | 8              |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [287](#event-287)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     22 |              6 |
| [65535.2](#event-655352) | 0x0018       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x1CB5F     |      117599 |
|       2 | 0xFFFFD428  |  4294956072 |
|       3 | 0xFFFFE0B7  |  4294959287 |
|       4 | 0x001E      |          30 |
|       5 | 0x1BC9A     |      113818 |
|       6 | 0xFFFFD46F  |  4294956143 |
|       7 | 0xFFFFE452  |  4294960210 |

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

### Event 287

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1F 00 01  80 02 80 03 80 1F 01 1E    2.............
0010: 03 C0 0F 01 1C 04 80 00                           ........        
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=117.599*, Z=-11.224*, Y=-8.009*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x1E] EventEntity looks at Gilgamesh (ID: 17809411/0x010FC003) and starts talking
  4: 0x0014 [0x1C] WAIT(30* ticks)
  5: 0x0017 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0018   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                          32 00 80 1F 00 05 80 06          2.......
0020: 80 07 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x0018 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x001B [0x1F] MOVE_ENTITY: EventEntity moves to X=113.818*, Z=-11.153*, Y=-7.086*
  2: 0x0023 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0025 [0x00] END_REQSTACK()
```
