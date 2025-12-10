# 17248899 - Karanka-Tonka

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | West Sarutabaruta (ID: 115) |
| Block Size       | 112 bytes                   |
| Total Events     | 6                           |
| References Count | 7                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |      1 |              1 |
| [65535.2](#event-655352) | 0x0002       |      1 |              1 |
| [65535.3](#event-655353) | 0x0003       |     24 |              6 |
| [65535.4](#event-655354) | 0x001B       |     14 |              4 |
| [65535.5](#event-655355) | 0x0029       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x1FDE      |        8158 |
|       2 | 0x5A1D      |       23069 |
|       3 | 0xFFFFFC18  |  4294966296 |
|       4 | 0x000A      |          10 |
|       5 | 0xFFFFFF0E  |  4294967054 |
|       6 | 0x7261      |       29281 |

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

### Event 65535.1

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

### Event 65535.2

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

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0003   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          32 00 80 1F 00  01 80 02 80 03 80 1F 01     2............
0010: 6F 4A 83 32 07 01 80 32  07 01 00                 oJ.2...2...     
```

#### Opcodes

```
  0: 0x0003 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0006 [0x1F] MOVE_ENTITY: EventEntity moves to X=8.158*, Z=23.069*, Y=-1.000*
  2: 0x000E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0010 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0011 [0x4A] Karanka-Tonka (ID: 17248899/0x01073283) looks at Khoto Rokkorah (ID: 17248896/0x01073280)
  5: 0x001A [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001B   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                   32 04 80 1F 00             2....
0020: 05 80 06 80 03 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x001B [0x32] ExtData[1]->MainSpeed = 10* * 0.1
  1: 0x001E [0x1F] MOVE_ENTITY: EventEntity moves to X=-0.242*, Z=29.281*, Y=-1.000*
  2: 0x0026 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0028 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0029  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             00                             .      
```

#### Opcodes

```
  0: 0x0029 [0x00] END_REQSTACK()
```
