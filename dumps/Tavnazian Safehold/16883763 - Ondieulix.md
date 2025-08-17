# 16883763 - Ondieulix

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Tavnazian Safehold (ID: 26) |
| Block Size       | 112 bytes                   |
| Total Events     | 4                           |
| References Count | 8                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [113](#event-113)        | 0x0001       |     13 |              3 |
| [65535.1](#event-655351) | 0x000E       |     24 |              5 |
| [65535.2](#event-655352) | 0x0026       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x0981      |        2433 |
|       2 | 0x63E1      |       25569 |
|       3 | 0xFFFFA6E2  |  4294944482 |
|       4 | 0x1384      |        4996 |
|       5 | 0x5C04      |       23556 |
|       6 | 0xFFFFA74F  |  4294944591 |
|       7 | 0x0B77      |        2935 |

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

### Event 113

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 94  01 F8 FF FF 7F 00         .............  
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x000D [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000E   |
| Data Size    | 24 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            79 00                y.
0010: F8 FF FF 7F 28 A0 01 01  32 00 80 1F 00 01 80 02  ....(...2.......
0020: 80 03 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x000E [0x79] EventEntity looks at Prishe (ID: 16883752/0x0101A028) (Basic look)
  1: 0x0018 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x001B [0x1F] MOVE_ENTITY: EventEntity moves to X=2.433*, Z=25.569*, Y=-22.814*
  3: 0x0023 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0025 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0026   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   37 04  80 05 80 06 80 07 80 00        7.........
```

#### Opcodes

```
  0: 0x0026 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=4.996*, z=23.556*, y=-22.705*, direction=258.0°*
  1: 0x002F [0x00] END_REQSTACK()
```
