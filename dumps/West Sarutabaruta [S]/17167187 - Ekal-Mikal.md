# 17167187 - Ekal-Mikal

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | West Sarutabaruta [S] (ID: 95) |
| Block Size       | 108 bytes                      |
| Total Events     | 5                              |
| References Count | 7                              |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [102](#event-102)        | 0x0001       |      1 |              1 |
| [103](#event-103)        | 0x0002       |      1 |              1 |
| [65535.1](#event-655351) | 0x0003       |     20 |              6 |
| [65535.2](#event-655352) | 0x0017       |     20 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x225A2     |      140706 |
|       2 | 0x51D4D     |      335181 |
|       3 | 0xFFFF6DEC  |  4294929900 |
|       4 | 0xFFFA4022  |  4294590498 |
|       5 | 0xFFF97A5F  |  4294539871 |
|       6 | 0x1F55      |        8021 |

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

### Event 102

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

### Event 103

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
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          32 00 80 1F 00  01 80 02 80 03 80 1F 01     2............
0010: 6F 1E 52 F3 05 01 00                              o.R....         
```

#### Opcodes

```
  0: 0x0003 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0006 [0x1F] MOVE_ENTITY: EventEntity moves to X=140.706*, Z=335.181*, Y=-37.396*
  2: 0x000E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0010 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0011 [0x1E] EventEntity looks at Lehko Habhoka (ID: 17167186/0x0105F352) and starts talking
  5: 0x0016 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      32  00 80 1F 00 04 80 05 80         2........
0020: 06 80 1F 01 6F 1E 52 F3  05 01 00                 ....o.R....     
```

#### Opcodes

```
  0: 0x0017 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x001A [0x1F] MOVE_ENTITY: EventEntity moves to X=-376.798*, Z=-427.425*, Y=8.021*
  2: 0x0022 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0024 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0025 [0x1E] EventEntity looks at Lehko Habhoka (ID: 17167186/0x0105F352) and starts talking
  5: 0x002A [0x00] END_REQSTACK()
```
