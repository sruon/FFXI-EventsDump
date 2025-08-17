# 17399856 - Yagudo Avatar

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Altar Room (ID: 152) |
| Block Size       | 84 bytes             |
| Total Events     | 3                    |
| References Count | 8                    |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [48](#event-48)       | 0x0001       |     10 |              2 |
| [49](#event-49)       | 0x000B       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFB21B0  |  4294648240 |
|       1 | 0x1828      |        6184 |
|       2 | 0x5DC0      |       24000 |
|       3 | 0x05E2      |        1506 |
|       4 | 0xFFFB22E3  |  4294648547 |
|       5 | 0x1698      |        5784 |
|       6 | 0x5DBF      |       23999 |
|       7 | 0x0DAC      |        3500 |

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

### Event 48

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    37 00 80 01 80 02 80  03 80 00                  7.........     
```

#### Opcodes

```
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-319.056*, z=6.184*, y=24.000*, direction=132.4°*
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 49

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000B   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   37 04 80 05 80             7....
0010: 06 80 07 80 00                                    .....           
```

#### Opcodes

```
  0: 0x000B [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-318.749*, z=5.784*, y=23.999*, direction=307.6°*
  1: 0x0014 [0x00] END_REQSTACK()
```
