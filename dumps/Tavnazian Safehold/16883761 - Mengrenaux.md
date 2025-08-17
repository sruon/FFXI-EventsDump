# 16883761 - Mengrenaux

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Tavnazian Safehold (ID: 26) |
| Block Size       | 100 bytes                   |
| Total Events     | 4                           |
| References Count | 7                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [113](#event-113)        | 0x0001       |     13 |              3 |
| [65535.1](#event-655351) | 0x000E       |     10 |              2 |
| [65535.2](#event-655352) | 0x0018       |     15 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFFF414  |  4294964244 |
|       1 | 0x769E      |       30366 |
|       2 | 0xFFFFA434  |  4294943796 |
|       3 | 0x0E96      |        3734 |
|       4 | 0x000D      |          13 |
|       5 | 0xFFFFF80C  |  4294965260 |
|       6 | 0x78A0      |       30880 |

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
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            37 00                7.
0010: 80 01 80 02 80 03 80 00                           ........        
```

#### Opcodes

```
  0: 0x000E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-3.052*, z=30.366*, y=-23.500*, direction=328.2°*
  1: 0x0017 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0018   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                          32 04 80 1F 00 05 80 06          2.......
0020: 80 02 80 1F 01 6F 00                              .....o.         
```

#### Opcodes

```
  0: 0x0018 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x001B [0x1F] MOVE_ENTITY: EventEntity moves to X=-2.036*, Z=30.880*, Y=-23.500*
  2: 0x0023 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0025 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0026 [0x00] END_REQSTACK()
```
