# 16839231 - Repair Trunk

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Abyssea - Konschtat (ID: 15) |
| Block Size       | 48 bytes                     |
| Total Events     | 2                            |
| References Count | 2                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [221](#event-221)     | 0x0001       |     12 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0626      |        1574 |
|       1 | 0x1F89      |        8073 |

## String References

- **8073**: The casket is filled to the brim with $5.

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

### Event 221

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 12 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 03 02 10 00 80 48  01 80 23 21 00            B.....H..#!.   
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x03] Work_Zone[2] = 1574*
  2: 0x0007 [0x48] [System] [8073*]:
    → "The casket is filled to the brim with $5."
  3: 0x000A [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x000B [0x21] END_EVENT
  5: 0x000C [0x00] END_REQSTACK()
```
