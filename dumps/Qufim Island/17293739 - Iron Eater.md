# 17293739 - Iron Eater

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Qufim Island (ID: 126) |
| Block Size       | 88 bytes               |
| Total Events     | 3                      |
| References Count | 8                      |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [100](#event-100)        | 0x0001       |     10 |              2 |
| [65535.1](#event-655351) | 0x000B       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFF65F34  |  4294336308 |
|       1 | 0x6F9A0     |      457120 |
|       2 | 0x423C      |       16956 |
|       3 | 0x0C85      |        3205 |
|       4 | 0x000D      |          13 |
|       5 | 0xFFF69B11  |  4294351633 |
|       6 | 0x70BA9     |      461737 |
|       7 | 0x3489      |       13449 |

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
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-630.988*, z=457.120*, y=16.956*, direction=281.7°*
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000B   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   32 04 80 1F 00             2....
0010: 05 80 06 80 07 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x000B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x000E [0x1F] MOVE_ENTITY: EventEntity moves to X=-615.663*, Z=461.737*, Y=13.449*
  2: 0x0016 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0018 [0x00] END_REQSTACK()
```
