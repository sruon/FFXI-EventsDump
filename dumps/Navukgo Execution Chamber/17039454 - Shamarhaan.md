# 17039454 - Shamarhaan

## Common Data

| Field            | Value                              |
|------------------|------------------------------------|
| Zone             | Navukgo Execution Chamber (ID: 64) |
| Block Size       | 68 bytes                           |
| Total Events     | 3                                  |
| References Count | 4                                  |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [32000](#event-32000) | 0x0001       |     10 |              2 |
| [32001](#event-32001) | 0x000B       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x5C39E     |      377758 |
|       1 | 0x5CCBC     |      380092 |
|       2 | 0xFFFE3AE1  |  4294851297 |
|       3 | 0x07F6      |        2038 |

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

### Event 32000

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
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=377.758*, z=380.092*, y=-115.999*, direction=179.1°*
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 32001

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000B   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   37 00 80 01 80             7....
0010: 02 80 03 80 00                                    .....           
```

#### Opcodes

```
  0: 0x000B [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=377.758*, z=380.092*, y=-115.999*, direction=179.1°*
  1: 0x0014 [0x00] END_REQSTACK()
```
