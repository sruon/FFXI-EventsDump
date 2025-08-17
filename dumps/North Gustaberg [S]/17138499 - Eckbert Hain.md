# 17138499 - Eckbert Hain

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | North Gustaberg [S] (ID: 88) |
| Block Size       | 144 bytes                    |
| Total Events     | 6                            |
| References Count | 10                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [205](#event-205)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     25 |              3 |
| [65535.2](#event-655352) | 0x001B       |      7 |              2 |
| [65535.3](#event-655353) | 0x0022       |     14 |              4 |
| [65535.4](#event-655354) | 0x0030       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0002      |           2 |
|       1 | 0x0000      |           0 |
|       2 | 0x0001      |           1 |
|       3 | 0x0050      |          80 |
|       4 | 0x4F606     |      325126 |
|       5 | 0xE4045     |      933957 |
|       6 | 0xFFFFAE55  |  4294946389 |
|       7 | 0x4BC96     |      310422 |
|       8 | 0xE1115     |      921877 |
|       9 | 0xFFFFB546  |  4294948166 |

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

### Event 205

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
| Data Size    | 25 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       7E 06 F8 FF FF 7F  00 80 01 80 01 80 01 80    ~.............
0010: 01 80 02 80 7E 04 F8 FF  FF 7F 00                 ....~......     
```

#### Opcodes

```
  0: 0x0002 [0x7E] CHOCOBO_MOUNT: Mode 6 (custom mount) on EventEntity
  1: 0x0014 [0x7E] CHOCOBO_MOUNT: Mode 4 on EventEntity
  2: 0x001A [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001B  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                   7E 05 F8 FF FF             ~....
0020: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x001B [0x7E] CHOCOBO_MOUNT: Dismount EventEntity (status = 0)
  1: 0x0021 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0022   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:       32 03 80 1F 00 04  80 05 80 06 80 1F 01 00    2.............
```

#### Opcodes

```
  0: 0x0022 [0x32] ExtData[1]->MainSpeed = 80* * 0.1
  1: 0x0025 [0x1F] MOVE_ENTITY: EventEntity moves to X=325.126*, Z=933.957*, Y=-20.907*
  2: 0x002D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002F [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 32 03 80 1F 00 07 80 08  80 09 80 1F 01 00        2.............  
```

#### Opcodes

```
  0: 0x0030 [0x32] ExtData[1]->MainSpeed = 80* * 0.1
  1: 0x0033 [0x1F] MOVE_ENTITY: EventEntity moves to X=310.422*, Z=921.877*, Y=-19.130*
  2: 0x003B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003D [0x00] END_REQSTACK()
```
