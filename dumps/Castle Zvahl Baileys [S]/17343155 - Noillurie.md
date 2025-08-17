# 17343155 - Noillurie

## Common Data

| Field            | Value                              |
|------------------|------------------------------------|
| Zone             | Castle Zvahl Baileys [S] (ID: 138) |
| Block Size       | 140 bytes                          |
| Total Events     | 6                                  |
| References Count | 10                                 |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [3](#event-3)            | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     10 |              2 |
| [65535.2](#event-655352) | 0x000C       |     10 |              2 |
| [65535.3](#event-655353) | 0x0016       |     21 |              5 |
| [65535.4](#event-655354) | 0x002B       |     16 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x21FFB     |      139259 |
|       4 | 0x103A3     |       66467 |
|       5 | 0xFFFFA209  |  4294943241 |
|       6 | 0x22851     |      141393 |
|       7 | 0x158FD     |       88317 |
|       8 | 0xFFFFA0AC  |  4294942892 |
|       9 | 0x0B4E      |        2894 |

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

### Event 3

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
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       6C B3 A2 08 01 00  80 01 80 00                l.........    
```

#### Opcodes

```
  0: 0x0002 [0x6C] FADE_ENTITY_COLOR(entity_id=Noillurie (ID: 17343155/0x0108A2B3), end_alpha=0*, fade_time=1*)
  1: 0x000B [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000C   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      6C B3 A2 08              l...
0010: 01 02 80 01 80 00                                 ......          
```

#### Opcodes

```
  0: 0x000C [0x6C] FADE_ENTITY_COLOR(entity_id=Noillurie (ID: 17343155/0x0108A2B3), end_alpha=128*, fade_time=1*)
  1: 0x0015 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0016   |
| Data Size    | 21 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                   1F 00  03 80 04 80 05 80 1F 01        ..........
0020: 1F 00 06 80 07 80 08 80  1F 01 00                 ...........     
```

#### Opcodes

```
  0: 0x0016 [0x1F] MOVE_ENTITY: EventEntity moves to X=139.259*, Z=66.467*, Y=-24.055*
  1: 0x001E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0020 [0x1F] MOVE_ENTITY: EventEntity moves to X=141.393*, Z=88.317*, Y=-24.404*
  3: 0x0028 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x002A [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002B   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   5B 09 80 B3 A2             [....
0030: 08 01 B3 A2 08 01 6E 79  72 30 00                 ......nyr0.     
```

#### Opcodes

```
  0: 0x002B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "nyr0" with entities [Noillurie (ID: 17343155/0x0108A2B3), Noillurie (ID: 17343155/0x0108A2B3)], work=2894*
  1: 0x003A [0x00] END_REQSTACK()
```
