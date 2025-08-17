# 17494724 - Gravestone

## Common Data

| Field            | Value                                |
|------------------|--------------------------------------|
| Zone             | The Eldieme Necropolis [S] (ID: 175) |
| Block Size       | 36 bytes                             |
| Total Events     | 2                                    |
| References Count | 1                                    |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [4](#event-4)         | 0x0001       |      7 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1DBF      |        7615 |

## String References

- **7615**: You find a piece of the map by the base of the gravestone!

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

### Event 4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 7 bytes |
| Instructions | 5       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 48 00 80 23 21 00                            BH..#!.        
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x48] [System] [7615*]:
    → "You find a piece of the map by the base of the gravestone!"
  2: 0x0005 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0006 [0x21] END_EVENT
  4: 0x0007 [0x00] END_REQSTACK()
```
