# 16982442 - Mihli Aliapoh

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Aht Urhgan Whitegate2 (ID: 50) |
| Block Size       | 128 bytes                      |
| Total Events     | 5                              |
| References Count | 10                             |

## List of Events

| Event ID                  | Entrypoint   |   Size |   Instructions |
|---------------------------|--------------|--------|----------------|
| [65535](#event-65535)     | 0x0000       |      1 |              1 |
| [896](#event-896)         | 0x0001       |      1 |              1 |
| [65535.1](#event-65535-1) | 0x0002       |     12 |              3 |
| [65535.2](#event-65535-2) | 0x000E       |     20 |              6 |
| [65535.3](#event-65535-3) | 0x0022       |     15 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFD4F      |       64847 |
|       1 | 0x5D0A      |       23818 |
|       2 | 0xFFFFE822  |  4294961186 |
|       3 | 0x039B      |         923 |
|       4 | 0x000D      |          13 |
|       5 | 0x10683     |       67203 |
|       6 | 0x4405      |       17413 |
|       7 | 0x0000      |           0 |
|       8 | 0xF9F7      |       63991 |
|       9 | 0x273F      |       10047 |

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

### Event 896

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
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       33 01 37 00 80 01  80 02 80 03 80 00          3.7.........  
```

#### Opcodes

```
  0: 0x0002 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0004 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=64.847*, z=23.818*, y=-6.110*, direction=81.1°*
  2: 0x000D [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000E   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            32 04                2.
0010: 80 1F 00 05 80 06 80 07  80 1F 01 6F 1E C8 20 03  ...........o.. .
0020: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x000E [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0011 [0x1F] MOVE_ENTITY: EventEntity moves to X=67.203*, Z=17.413*, Y=0.000*
  2: 0x0019 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x001C [0x1E] EventEntity looks at Aphmau (ID: 16982216/0x010320C8) and starts talking
  5: 0x0021 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0022   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:       32 04 80 1F 00 08  80 09 80 07 80 1F 01 6F    2............o
0030: 00                                                .               
```

#### Opcodes

```
  0: 0x0022 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0025 [0x1F] MOVE_ENTITY: EventEntity moves to X=63.991*, Z=10.047*, Y=0.000*
  2: 0x002D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0030 [0x00] END_REQSTACK()
```
