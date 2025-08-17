# 17031679 - Operating Lever

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Halvung (ID: 62) |
| Block Size       | 56 bytes         |
| Total Events     | 2                |
| References Count | 3                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [104](#event-104)     | 0x0001       |     19 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x012C      |         300 |
|       1 | 0x1EF1      |        7921 |
|       2 | 0x1EF2      |        7922 |

## String References

- **7921**: <Player>'s hand has grown numb...
- **7922**: <Player> can't hold on for much longer...

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

### Event 104

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 19 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 1C 00 80 48 01  80 1C 00 80 48 02 80 1C    ....H.....H...
0010: 00 80 21 00                                       ..!.            
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x1C] WAIT(300* ticks)
  2: 0x0006 [0x48] [System] [7921*]:
    → "<Player>'s hand has grown numb..."
  3: 0x0009 [0x1C] WAIT(300* ticks)
  4: 0x000C [0x48] [System] [7922*]:
    → "<Player> can't hold on for much longer..."
  5: 0x000F [0x1C] WAIT(300* ticks)
  6: 0x0012 [0x21] END_EVENT
  7: 0x0013 [0x00] END_REQSTACK()
```
