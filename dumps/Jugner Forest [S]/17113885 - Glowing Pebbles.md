# 17113885 - Glowing Pebbles

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Jugner Forest [S] (ID: 82) |
| Block Size       | 64 bytes                   |
| Total Events     | 3                          |
| References Count | 4                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [100](#event-100)     | 0x0001       |      1 |              1 |
| [106](#event-106)     | 0x0002       |     15 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1A608     |      108040 |
|       1 | 0x6ABDC     |      437212 |
|       2 | 0x0ED3      |        3795 |
|       3 | 0x0617      |        1559 |

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

### Event 100

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

### Event 106

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 15 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       37 00 80 01 80 02  80 03 80 80 F8 FF FF 7F    7.............
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0002 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=108.040*, z=437.212*, y=3.795*, direction=137.0°*
  1: 0x000B [0x80] LOAD_WAIT(entity=EventEntity)
  2: 0x0010 [0x00] END_REQSTACK()
```
