# 17105500 - Tihl Midurhi

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Southern San d'Oria [S] (ID: 80) |
| Block Size       | 136 bytes                        |
| Total Events     | 6                                |
| References Count | 9                                |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [63](#event-63)          | 0x0001       |      1 |              1 |
| [62](#event-62)          | 0x0002       |      1 |              1 |
| [65535.1](#event-655351) | 0x0003       |     15 |              5 |
| [65535.2](#event-655352) | 0x0012       |     15 |              5 |
| [65535.3](#event-655353) | 0x0021       |     25 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x18BAB     |      101291 |
|       2 | 0xFFFF4E32  |  4294921778 |
|       3 | 0x03E7      |         999 |
|       4 | 0x247AA     |      149418 |
|       5 | 0x97A2      |       38818 |
|       6 | 0x0000      |           0 |
|       7 | 0x0003      |           3 |
|       8 | 0x0001      |           1 |

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

### Event 63

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

### Event 62

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
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          32 00 80 1F 00  01 80 02 80 03 80 1F 01     2............
0010: 6F 00                                             o.              
```

#### Opcodes

```
  0: 0x0003 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0006 [0x1F] MOVE_ENTITY: EventEntity moves to X=101.291*, Z=-45.518*, Y=0.999*
  2: 0x000E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0010 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0011 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0012   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:       32 00 80 1F 00 04  80 05 80 06 80 1F 01 6F    2............o
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x0012 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0015 [0x1F] MOVE_ENTITY: EventEntity moves to X=149.418*, Z=38.818*, Y=0.000*
  2: 0x001D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0020 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0021   |
| Data Size    | 25 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    7E 06 5C 02 05 01 07  80 06 80 08 80 08 80 08   ~.\............
0030: 80 08 80 7E 04 5C 02 05  01 00                    ...~.\....      
```

#### Opcodes

```
  0: 0x0021 [0x7E] CHOCOBO_MOUNT: Mode 6 (custom mount) on Tihl Midurhi (ID: 17105500/0x0105025C)
  1: 0x0033 [0x7E] CHOCOBO_MOUNT: Mode 4 on Tihl Midurhi (ID: 17105500/0x0105025C)
  2: 0x0039 [0x00] END_REQSTACK()
```
