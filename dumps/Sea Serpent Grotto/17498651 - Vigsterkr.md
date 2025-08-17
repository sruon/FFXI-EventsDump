# 17498651 - Vigsterkr

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Sea Serpent Grotto (ID: 176) |
| Block Size       | 52 bytes                     |
| Total Events     | 3                            |
| References Count | 1                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [18](#event-18)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     16 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0009      |           9 |

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

### Event 18

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
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       66 00 80 1B 02 0B  01 1B 02 0B 01 73 69 74    f..........sit
0010: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x0002 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sit0" with entities [Vigsterkr (ID: 17498651/0x010B021B), Vigsterkr (ID: 17498651/0x010B021B)], work=9*
  1: 0x0011 [0x00] END_REQSTACK()
```
