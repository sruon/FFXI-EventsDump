# 17162802 - Pattna-Ottna

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Windurst Waters [S] (ID: 94) |
| Block Size       | 112 bytes                    |
| Total Events     | 5                            |
| References Count | 9                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [151](#event-151)        | 0x0001       |      1 |              1 |
| [23](#event-23)          | 0x0002       |      1 |              1 |
| [65535.1](#event-655351) | 0x0003       |     22 |              6 |
| [65535.2](#event-655352) | 0x0019       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00F0      |         240 |
|       1 | 0x000D      |          13 |
|       2 | 0xFFFFF5AB  |  4294964651 |
|       3 | 0xFFFFE3C7  |  4294960071 |
|       4 | 0xFFFF9C65  |  4294941797 |
|       5 | 0x0023      |          35 |
|       6 | 0x7189      |       29065 |
|       7 | 0x09DC      |        2524 |
|       8 | 0xFFFF9A71  |  4294941297 |

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

### Event 151

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

### Event 23

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
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          1C 00 80 32 01  80 1F 00 02 80 03 80 04     ...2.........
0010: 80 1F 01 1E 9D E2 05 01  00                       .........       
```

#### Opcodes

```
  0: 0x0003 [0x1C] WAIT(240* ticks)
  1: 0x0006 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0009 [0x1F] MOVE_ENTITY: EventEntity moves to X=-2.645*, Z=-7.225*, Y=-25.499*
  3: 0x0011 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0013 [0x1E] EventEntity looks at Karaha-Baruha (ID: 17162909/0x0105E29D) and starts talking
  5: 0x0018 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0019   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             32 05 80 1F 00 06 80           2......
0020: 07 80 08 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x0019 [0x32] ExtData[1]->MainSpeed = 35* * 0.1
  1: 0x001C [0x1F] MOVE_ENTITY: EventEntity moves to X=29.065*, Z=2.524*, Y=-25.999*
  2: 0x0024 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0026 [0x00] END_REQSTACK()
```
