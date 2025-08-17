# 17772765 - Degenhard

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Ru'Lude Gardens (ID: 243) |
| Block Size       | 164 bytes                 |
| Total Events     | 7                         |
| References Count | 8                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [10137](#event-10137)    | 0x0001       |      1 |              1 |
| [10161](#event-10161)    | 0x0002       |      1 |              1 |
| [65535.1](#event-655351) | 0x0003       |     14 |              4 |
| [65535.2](#event-655352) | 0x0011       |     19 |              5 |
| [65535.3](#event-655353) | 0x0024       |     26 |              4 |
| [65535.4](#event-655354) | 0x003E       |     26 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000A      |          10 |
|       1 | 0x0AD3      |        2771 |
|       2 | 0x1C89B     |      116891 |
|       3 | 0x0C1D      |        3101 |
|       4 | 0x0008      |           8 |
|       5 | 0x192D      |        6445 |
|       6 | 0x1CEAC     |      118444 |
|       7 | 0x0C1C      |        3100 |

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

### Event 10137

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

### Event 10161

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

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0003   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          32 00 80 1F 00  01 80 02 80 03 80 1F 01     2............
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0003 [0x32] ExtData[1]->MainSpeed = 10* * 0.1
  1: 0x0006 [0x1F] MOVE_ENTITY: EventEntity moves to X=2.771*, Z=116.891*, Y=3.101*
  2: 0x000E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    32 04 80 1F 00 05 80  06 80 07 80 1F 01 1E 32   2.............2
0020: 30 0F 01 00                                       0...            
```

#### Opcodes

```
  0: 0x0011 [0x32] ExtData[1]->MainSpeed = 8* * 0.1
  1: 0x0014 [0x1F] MOVE_ENTITY: EventEntity moves to X=6.445*, Z=118.444*, Y=3.100*
  2: 0x001C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001E [0x1E] EventEntity looks at Maat (ID: 17772594/0x010F3032) and starts talking
  4: 0x0023 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0024   |
| Data Size    | 26 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             B4 00 00 00  3F 3F 3F 00 00 00 00 00      ....???.....
0030: 00 00 00 00 00 00 00 00  B5 00 00 00 00 00        ..............  
```

#### Opcodes

```
  0: 0x0024 [0xB4] UI_WINDOW_STRING_HANDLER(case=0x00 - Copy string from opcode, work_offset=ExtData[1]->WorkLocal[0], string="???")
  1: 0x0038 [0xB5] SET_EVENT_ENTITY_NAME: Change EventEntity name to ExtData[1]->WorkLocal[0]
  2: 0x003C [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x003D [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003E   |
| Data Size    | 26 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                            B4 00                ..
0040: 00 00 44 65 67 65 6E 68  61 72 64 00 00 00 00 00  ..Degenhard.....
0050: 00 00 B5 00 00 00 00 00                           ........        
```

#### Opcodes

```
  0: 0x003E [0xB4] UI_WINDOW_STRING_HANDLER(case=0x00 - Copy string from opcode, work_offset=ExtData[1]->WorkLocal[0], string="Degenhard")
  1: 0x0052 [0xB5] SET_EVENT_ENTITY_NAME: Change EventEntity name to ExtData[1]->WorkLocal[0]
  2: 0x0056 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0057 [0x00] END_REQSTACK()
```
