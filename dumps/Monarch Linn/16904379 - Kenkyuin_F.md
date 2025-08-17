# 16904379 - Kenkyuin_F

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Monarch Linn (ID: 31) |
| Block Size       | 124 bytes             |
| Total Events     | 5                     |
| References Count | 6                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [15](#event-15)          | 0x0001       |     13 |              3 |
| [65535.1](#event-655351) | 0x000E       |     10 |              2 |
| [65535.2](#event-655352) | 0x0018       |     24 |              5 |
| [32001](#event-32001)    | 0x0030       |     13 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0AF0      |        2800 |
|       1 | 0xFFFE36F8  |  4294850296 |
|       2 | 0xFFFF7555  |  4294931797 |
|       3 | 0x0800      |        2048 |
|       4 | 0x000D      |          13 |
|       5 | 0x0578      |        1400 |

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

### Event 15

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
  0: 0x000E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=2.800*, z=-117.000*, y=-35.499*, direction=180.0°*
  1: 0x0017 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0018   |
| Data Size    | 24 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                          79 00 BB F0 01 01 B4 F0          y.......
0020: 01 01 32 04 80 1F 00 05  80 01 80 02 80 1F 01 00  ..2.............
```

#### Opcodes

```
  0: 0x0018 [0x79] Kenkyuin_F (ID: 16904379/0x0101F0BB) looks at Nag'molada (ID: 16904372/0x0101F0B4) (Basic look)
  1: 0x0022 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0025 [0x1F] MOVE_ENTITY: EventEntity moves to X=1.400*, Z=-117.000*, Y=-35.499*
  3: 0x002D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x002F [0x00] END_REQSTACK()
```

### Event 32001

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 92 01 F8 FF FF 7F 94 01  F8 FF FF 7F 00           .............   
```

#### Opcodes

```
  0: 0x0030 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0036 [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x003C [0x00] END_REQSTACK()
```
