# 17879416 - Magma Vein

## Common Data

| Field            | Value               |
|------------------|---------------------|
| Zone             | Moh Gates (ID: 269) |
| Block Size       | 44 bytes            |
| Total Events     | 2                   |
| References Count | 2                   |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [2500](#event-2500)   | 0x0001       |     11 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1D48      |        7496 |
|       1 | 0x1D49      |        7497 |

## String References

- **7496**: A strange energy rises forth from the magma.
- **7497**: You write down your findings.

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

### Event 2500

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 11 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 48 00 80 23 48 01  80 23 21 00               BH..#H..#!.    
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x48] [System] [7496*]:
    → "A strange energy rises forth from the magma."
  2: 0x0005 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0006 [0x48] [System] [7497*]:
    → "You write down your findings."
  4: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000A [0x21] END_EVENT
  6: 0x000B [0x00] END_REQSTACK()
```
