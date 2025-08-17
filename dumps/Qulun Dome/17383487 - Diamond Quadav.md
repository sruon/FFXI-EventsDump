# 17383487 - Diamond Quadav

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Qulun Dome (ID: 148) |
| Block Size       | 84 bytes             |
| Total Events     | 3                    |
| References Count | 8                    |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [62](#event-62)       | 0x0001       |     10 |              2 |
| [63](#event-63)       | 0x000B       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2EE3      |       12003 |
|       1 | 0xFFFF4901  |  4294920449 |
|       2 | 0x640F      |       25615 |
|       3 | 0x0560      |        1376 |
|       4 | 0x2152      |        8530 |
|       5 | 0xFFFF4608  |  4294919688 |
|       6 | 0x6369      |       25449 |
|       7 | 0x0425      |        1061 |

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

### Event 62

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
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=12.003*, z=-46.847*, y=25.615*, direction=120.9°*
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 63

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
  0: 0x000B [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=8.530*, z=-47.608*, y=25.449*, direction=93.2°*
  1: 0x0014 [0x00] END_REQSTACK()
```
